from cmath import pi
import numpy as np
from numpy import interp
from numpy import pi
import rospy
import roboticstoolbox as rt
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


#Función que cambia valores de registros de los motores del Pincher.
def jointCommand(command, id_num, addr_name, value, time):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

def ActualizarRegistros(P_o):
    for i in range(len(P_o)):
        jointCommand('', (i+1), 'Goal_Position', int(P_o[i]), 0)
        s=i
    print(P_o)

#Función que permite realizar cambios en los 5 motores con entradas de ángulos en radianes
def joint_publisher(q,t):
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
    point = JointTrajectoryPoint()
    point.positions = q 
    point.time_from_start = rospy.Duration(t)
    state.points.append(point)
    pub.publish(state)
    print('Cambio de punto q:')  

    CinDir(q[0],q[1],q[2],q[3],q[4])
    time.sleep(3*t)

#Se crea el publisher para poder enviar datos
pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
rospy.init_node('joint_publisher', anonymous=False)
state = JointTrajectory() 
state.header.stamp = rospy.Time.now()
state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_4"]



#Arreglo de offsets de Home
OffsetHomG=np.array([0,0,-90,0,0])
OffsetHomR=np.multiply(OffsetHomG,np.pi/180)


# Funcion de cinemática inversa de q 1
def q_1(P_x,P_y):
    return np.arctan2(P_y,P_x)

# Funcion de cinemática inversa de q 2
def q_2(P_x,P_y,P_z,ang,L_1,L_2,L_3,L_4):
    R=np.sqrt(P_x**2+P_y**2)
    D_r=R-L_4*np.cos(ang)
    D_z=P_z-L_4*np.sin(ang)-L_1
    return -2*np.arctan((2*D_r*L_2 - np.sqrt(- D_r**4 - 2*D_r**2*D_z**2 + 2*D_r**2*L_2**2 + 2*D_r**2*L_3**2 - D_z**4 + 2*D_z**2*L_2**2 + 2*D_z**2*L_3**2 - L_2**4 + 2*L_2**2*L_3**2 - L_3**4))/(D_r**2 + D_z**2 + 2*D_z*L_2 + L_2**2 - L_3**2))

# Funcion de cinemática inversa de q 3
def q_3(P_x,P_y,P_z,ang,L_1,L_2,L_3,L_4):
    R=np.sqrt(P_x**2+P_y**2)
    D_r=R-L_4*np.cos(ang)
    D_z=P_z-L_4*np.sin(ang)-L_1
    return -2*np.arctan((np.sqrt((- D_r**2 - D_z**2 + L_2**2 + 2*L_2*L_3 + L_3**2)*(D_r**2 + D_z**2 - L_2**2 + 2*L_2*L_3 - L_3**2)) - 2*L_2*L_3)/(D_r**2 + D_z**2 - L_2**2 - L_3**2))

# Funcion de cinemática inversa de q 4
def q_4(ang,q_2,q_3):
    return ang-q_2-q_3

# Funcion de cinemática inversa del pincher
def CinInv(P_x,P_y,P_z,ang):
    L_1=0.134
    L_2=0.105
    L_3=0.105
    L_4=0.067
    T1=q_1(P_x,P_y)
    T2=q_2(P_x,P_y,P_z,ang,L_1,L_2,L_3,L_4)
    T3=q_3(P_x,P_y,P_z,ang,L_1,L_2,L_3,L_4)
    T4=q_4(ang,T2,T3)
    return np.array([round(T1,3),round(T2,3),round(T3,3),round(T4,3)])

# Funcion de cinemática directa del Pincher
def CinDir(q_1,q_2,q_3,q_4,q_5):
    L_1=0.137
    L_2=0.105
    L_3=0.105
    L_4=0.095
    ang=np.arccos(np.cos(q_2 + q_3 + q_4)*np.cos(q_1))
    P_x=np.cos(q_1)*(L_3*np.cos(q_2 + q_3) - L_2*np.sin(q_2) + L_4*np.cos(q_2 + q_3 + q_4))
    P_y=np.sin(q_1)*(L_3*np.cos(q_2 + q_3) - L_2*np.sin(q_2) + L_4*np.cos(q_2 + q_3 + q_4))
    P_z=L_1 + L_3*np.sin(q_2 + q_3) + L_2*np.cos(q_2) + L_4*np.sin(q_2 + q_3 + q_4)
    if q_5<-40*np.pi/180:
        Grip=1
    else:
        Grip=0

    print("Coordenadas:")
    print('Pos X: '+"%.2f" % P_x+'°\tPos Y:'+"%.2f" % P_y+'°\tPos Z:'+"%.2f" % P_z+'°\tang:'+"%.2f" % ang)

    if Grip==1:
        print("\nq4 cerrado\n")
    else:
        print("\nq4 abierto\n")



#Función que permite realizar la trayectoria a un punto Pos en un tiempo t. Los sleep se realizan para no saturar el bus de comunicaciones
def Rut2p(Pos,t,tool):
    q=np.concatenate(((ikine4r(Pos[0],Pos[1],Pos[2],Pos[3])+OffsetHomR[0:4]),np.array([tool])), axis=0)
    time.sleep(2*t)
    joint_publisher(q,t)
    time.sleep(2*t)

#Función de impresión de opciones
def PrintOpciones():
    print("¿Qué desea hacer?:")
    print("1:\tIniciar rutina")
    print("2:\tSalir")


############################################################
############################################################


#Ángulos de posición home con y sin herramienta montada

posHome=np.array([0.2,0,0.25,0])

#Alturas Z en metros y ángulo de ataque ang

Zpiso=0.148
ZpisoInt=0.115
Zpiso2=0.165
Zportaherramientas=0.155
Zseguridad=0.2
Zseguridad2=0.25
ZseguridadPH=0.24
ang=0*np.pi/180
ang2=10*np.pi/180

#Posiciones de portaherramientas para carga y descarga
coorPortaHerramientasArriba=np.array([0.105,-0.23,ZseguridadPH,ang2])
coorPortaHerramientasAbajo=np.array([0.12,-0.24,Zportaherramientas,0])
coorPortaHerramientasAbajoDes=np.array([0.1,-0.21,Zportaherramientas,ang2])
#Angulos para arcos de espacio de trabajo diestro
lim=70*np.pi/180

#Valores de ángulo de cierre del gripper
gripClose=-100*np.pi/180
gripOpen=0

#Radios de espacio de trabajo mínimo y máximo
LimitMin=0.18
LimitMax=0.3

#Posiciones físicas del arco menor y mayor
LimitMin1=np.array([[LimitMin*np.cos(lim),LimitMin*np.sin(lim),Zseguridad,0],[LimitMin*np.cos(lim),LimitMin*np.sin(lim),ZpisoInt,0]])
LimitMin2=np.array([[LimitMin*np.cos(-lim),LimitMin*np.sin(-lim),ZpisoInt,0],[LimitMin*np.cos(-lim),LimitMin*np.sin(-lim),Zseguridad,0]])
LimitMax1=np.array([[LimitMax*np.cos(-lim),LimitMax*np.sin(-lim),Zseguridad,ang2],[LimitMax*np.cos(-lim),LimitMax*np.sin(-lim),Zpiso2-0.02,ang2]])
LimitMax2=np.array([[LimitMax*np.cos(lim),LimitMax*np.sin(lim),Zpiso2-0.02,ang2],[LimitMax*np.cos(lim),LimitMax*np.sin(lim),Zseguridad+0.015,ang2]])

# Mapa de puntos De iniciales, triángulo equilatero, rectas paralelas y los 5 puntos
desfa = 0.015
PuntosC=np.array([[0.250,0.110,Zseguridad-desfa, ang2],[0.250,0.110,Zpiso-desfa ,ang2],[0.250,0.150,Zpiso-desfa ,ang2],[0.200,0.150,Zpiso-desfa ,ang2],[0.2,0.11,Zpiso-desfa ,ang2],[0.2,0.11,Zpiso-desfa ,ang2],[0.2,0.11,Zseguridad-desfa ,ang2]])
PuntosJ=np.array([[0.250,0.100,Zseguridad+0.01-desfa,ang2],[0.250,0.100,Zpiso+0.01-desfa,ang2],[0.250,0.050,Zpiso+0.01-desfa,ang2],[0.250,0.075,Zpiso+0.01-desfa,ang2],[0.200,0.075,Zpiso-0.012-desfa,ang2],[0.200,0.100,Zpiso-0.012-desfa,ang2],[0.200,0.100,Zseguridad-desfa,ang2]])
PuntosD=np.array([[0.250,0.040,Zseguridad-desfa, ang2],[0.250,0.040,Zpiso-desfa ,ang2],[0.250,0,Zpiso-desfa ,ang2],[0.240,-0.01,Zpiso-desfa ,ang2],[0.21,-0.01,Zpiso-desfa ,ang2],[0.2,0,Zpiso-desfa ,ang2],[0.2,0.04,Zseguridad-desfa -0.07,ang2],[0.25,0.04,Zseguridad-desfa -0.07,ang2],[0.25,0.04,Zseguridad-desfa -0.07,ang2]])

Puntosojo1=np.array([[0.250,-0.02,Zseguridad-desfa, ang2],[0.250,-0.02,Zpiso-desfa ,ang2],[0.23,-0.04,Zpiso-desfa ,ang2],[0.21,-0.02,Zpiso-desfa ,ang2],[0.21,-0.02,Zpiso-desfa ,ang2]])
Puntosojo2=np.array([[0.250,-0.07,Zseguridad-desfa, ang2],[0.250,-0.07,Zpiso-desfa ,ang2],[0.230,-0.050,Zpiso-desfa ,ang2],[0.21,-0.07,Zpiso-desfa ,ang2],[0.21,-0.07,Zpiso-desfa ,ang2]])

############################################################

#Main
if __name__ == '__main__':
    try:

        #Definir los límites de torques (se dejan en el máximo)
        Torques=[1023,1023,1023,1023,1023]
        for i in range(5):    
            jointCommand('', (i+1), 'Torque_Limit', Torques[i], 0)

        print("Laboratorio 5 de Robótica")
        

        #Realizar ida al home
        Rut2p(posHome,1,gripOpen)
        #Inicialmente no está cargado
        Cargado=0
        caso=0

        while(caso!=2):
            PrintOpciones()
            #El usuario ingresa qué caso desea realizar. Solo puede iniciar cargado la herramienta.
            caso=int(input())
            if caso==1:
                if Cargado==0: 
                    print("Iniciando rutina")
                    start_time = time.time()

                    #Se realizan rutinas de movimiento a puntos de carga de seguridad y luego baja
                    Rut2p(coorPortaHerramientasArriba,0.3,gripOpen)
                    Rut2p(coorPortaHerramientasAbajo,0.5,gripOpen)
                    input()
                    #Se aprieta el gripper y se vuelve a home con el gripper cerrado
                    print("Apretar gripper")
                    Rut2p(coorPortaHerramientasAbajo,0.5,gripClose)
                    Rut2p(coorPortaHerramientasArriba,1,gripClose)
                    Rut2p(posHome,1,gripClose)

                    #Avisa una finalización de rutina al establecer el tiempo de ejecución de esta operación
                    end_time = time.time()
                    Tiempo=end_time-start_time
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    start_time = time.time()
                    Limites=[LimitMin1[0,:],LimitMin1[1,:],LimitMin2[0,:],LimitMin2[1,:],LimitMax1[0,:],LimitMax1[1,:],LimitMax2[0,:],LimitMax2[1,:],LimitMin1[0,:],posHome]
                    ArrTiempo=[1.5,0.5,0.5,0.5,1,2,1.5,2,0.5,1]
                    for i in range(len(Limites)):
                        Rut2p(Limites[i],ArrTiempo[i],gripClose)
                    #Finaliza volviendo al home
                    Rut2p(posHome,1.5,gripClose)

                    end_time = time.time()
                    Tiempo=end_time-start_time
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    start_time = time.time()
                    #Se realizan rutinas para la C, J y D
                    ArrTiempo=[1.5,1.5,1.5,0.5,0.5,0.5,1,1,1.5,0.5,0.5,0.5,0.5,1,1]
                    for i in range(7):
                        Rut2p(PuntosC[i,:],ArrTiempo[i],gripClose)
                    time.sleep(1)
                    for i in range(7):
                        Rut2p(PuntosJ[i,:],ArrTiempo[i],gripClose)
                    for i in range(9):
                        Rut2p(PuntosD[i,:],ArrTiempo[i],gripClose)
                    Rut2p(posHome,1.5,gripClose)

                    end_time = time.time()
                    Tiempo=end_time-start_time
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    start_time = time.time()
                    
                    #ojitos

                    ArrTiempo=[1.5,1.5,1.5,1.5,1.5]
                    for i in range(5):
                        Rut2p(Puntosojo1[i,:],ArrTiempo[i],gripClose)

                    for i in range(5):
                        Rut2p(Puntosojo2[i,:],ArrTiempo[i],gripClose)

                    #Se realizan 25 puntos para la boca

                    N=25
                    Rads=np.linspace(0,np.pi,N)
                    ZPuntos=np.ones(N)*(Zpiso)
                    angPuntos=np.ones(N)*ang2
                    t=0.2
                    ArrTiempo=np.ones(N)*t
                    #Se genera un arreglo de puntos X,Y,Z,ang para todos los N del círculo
                    PuntosCirc=np.zeros([N,4])
                    PuntosCirc[:,0]=0.2-0.025*np.sin(Rads)
                    PuntosCirc[:,1]=-0.025-0.025*np.cos(Rads)
                    PuntosCirc[:,2]=ZPuntos-0.02+0.005*np.cos(Rads)
                    PuntosCirc[:,3]=angPuntos

                    PuntosCirc2=np.zeros([N,4])
                    PuntosCirc2[:,0]=0.2-0.025*np.sin(Rads)
                    PuntosCirc2[:,1]=-0.075-0.025*np.cos(Rads)
                    PuntosCirc2[:,2]=ZPuntos-0.025+0.005*np.cos(Rads)
                    PuntosCirc2[:,3]=angPuntos

                    #Se establece una posición de inicio antes de empezar el círculo
                    PosIni=[0.2,0,Zseguridad2,ang2]

                    Rut2p(PosIni,1.5,gripClose)
                    
                    #Rutína de movimiento del círculo
                    for i in range(N):
                        Rut2p(PuntosCirc[i,:],ArrTiempo[i],gripClose)
                    
                    Rut2p(PosIni,1.5,gripClose)
                    for i in range(N):
                        Rut2p(PuntosCirc2[i,:],ArrTiempo[i],gripClose)
                    
                    #Vuelve a Home
                    Rut2p(posHome,2,gripClose)
                    start_time = time.time()
                    #Rutina para descargar la herramienta. Solo la realiza si está cargada.
                    Rut2p(coorPortaHerramientasArriba,0.3,gripClose)
                    Rut2p(coorPortaHerramientasAbajoDes,0.5,gripClose)
                    input()
                    print("Apretar gripper")
                    Rut2p(coorPortaHerramientasAbajoDes,0.5,gripOpen)
                    Rut2p(coorPortaHerramientasArriba,1,gripOpen)
                    Rut2p(posHome,1,gripOpen)

                    end_time = time.time()
                    Tiempo=end_time-start_time
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    Cargado=0
                else: 
                    print("La herramienta ya está cargada")
                
            
                
            elif caso==2:
                print("Se Finalizará el programa")
            
            else:
                print("Opción no válida. Saliendo.")
                break
        
        print("Finalizando rutinas")

    except rospy.ROSInterruptException:
        pass