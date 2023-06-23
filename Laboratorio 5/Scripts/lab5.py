from cmath import pi
import numpy as np
from numpy import pi
import rospy
import roboticstoolbox as rt
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


#Función para mover motores (de lab4).
def jointCommand(command, id_num, addr_name, value, time):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))
def ActualizarRegistros(Po):
    for i in range(len(Po)):
        jointCommand('', (i+1), 'Goal_Position', int(Po[i]), 0)
        s=i
    print(Po)

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

#Función para enviar datos
pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
rospy.init_node('joint_publisher', anonymous=False)
state = JointTrajectory() 
state.header.stamp = rospy.Time.now()
state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_4"]

#Offsets de Home
OffsetHomG=np.array([0,0,-90,0,0])
OffsetHomR=np.multiply(OffsetHomG,np.pi/180)


# Funcion de cinemática inversa de q 1
def q_1(Px,Py):
    return np.arctan2(Py,Px)

# Funcion de cinemática inversa de q 2
def q_2(Px,Py,P_z,ang,L1,L2,L3,L4):
    R=np.sqrt(Px**2+Py**2)
    D_r=R-L4*np.cos(ang)
    D_z=P_z-L4*np.sin(ang)-L1
    return -2*np.arctan((2*D_r*L2 - np.sqrt(- D_r**4 - 2*D_r**2*D_z**2 + 2*D_r**2*L2**2 + 2*D_r**2*L3**2 - D_z**4 + 2*D_z**2*L2**2 + 2*D_z**2*L3**2 - L2**4 + 2*L2**2*L3**2 - L3**4))/(D_r**2 + D_z**2 + 2*D_z*L2 + L2**2 - L3**2))

# Funcion de cinemática inversa de q 3
def q_3(Px,Py,P_z,ang,L1,L2,L3,L4):
    R=np.sqrt(Px**2+Py**2)
    D_r=R-L4*np.cos(ang)
    D_z=P_z-L4*np.sin(ang)-L1
    return -2*np.arctan((np.sqrt((- D_r**2 - D_z**2 + L2**2 + 2*L2*L3 + L3**2)*(D_r**2 + D_z**2 - L2**2 + 2*L2*L3 - L3**2)) - 2*L2*L3)/(D_r**2 + D_z**2 - L2**2 - L3**2))

# Funcion de cinemática inversa de q 4
def q_4(ang,q_2,q_3):
    return ang-q_2-q_3

# Funcion de cinemática inversa
def CinInv(Px,Py,P_z,ang):
    L1=0.1342
    L2=0.1052
    L3=0.1052
    L4=0.0675
    T1=q_1(Px,Py)
    T2=q_2(Px,Py,P_z,ang,L1,L2,L3,L4)
    T3=q_3(Px,Py,P_z,ang,L1,L2,L3,L4)
    T4=q_4(ang,T2,T3)
    return np.array([round(T1,3),round(T2,3),round(T3,3),round(T4,3)])

# Funcion de cinemática directa
def CinDir(q_1,q_2,q_3,q_4,q_5):
    L1=0.1342
    L2=0.1052
    L3=0.1052
    L4=0.0675
    ang=np.arccos(np.cos(q_2 + q_3 + q_4)*np.cos(q_1))
    Px=np.cos(q_1)*(L3*np.cos(q_2 + q_3) - L2*np.sin(q_2) + L4*np.cos(q_2 + q_3 + q_4))
    Py=np.sin(q_1)*(L3*np.cos(q_2 + q_3) - L2*np.sin(q_2) + L4*np.cos(q_2 + q_3 + q_4))
    P_z=L1 + L3*np.sin(q_2 + q_3) + L2*np.cos(q_2) + L4*np.sin(q_2 + q_3 + q_4)
    if q_5<-40*np.pi/180:
        Grip=1
    else:
        Grip=0
    print('Pos X: '+"%.2f" % Px+'°\tPos Y:'+"%.2f" % Py+'°\tPos Z:'+"%.2f" % P_z+'°\tang:'+"%.2f" % ang)
    if Grip==1:
        print("\nq4 cerrado\n")
    else:
        print("\nq4 abierto\n")



#Función que permite realizar moverse
def Mover(Pos,t,tool):
    q=np.concatenate(((CinInv(Pos[0],Pos[1],Pos[2],Pos[3])+OffsetHomR[0:4]),np.array([tool])), axis=0)
    time.sleep(2*t)
    joint_publisher(q,t)
    time.sleep(2*t)

def PrintOpciones():
    print("¿Qué desea hacer?:")
    print("1:\tIniciar rutina")
    print("2:\tSalir")


############################################################
############################################################


#Ángulos de posición home con y sin herramienta montada

HomeP=np.array([0.2,0,0.25,0])

#Alturas Z en metros y ángulo de ataque ang

Zpiso=0.148
Zpiso1=0.115
Zpiso2=0.165
Zportaherramientas=0.155
Zseguridad=0.2
Zseguridad2=0.25
Zseguridad3=0.24
ang=0*np.pi/180
ang2=10*np.pi/180

#Posiciones de portaherramientas para carga y descarga
Herramienta1=np.array([0.105,-0.23,Zseguridad3,ang2])
Herramienta2=np.array([0.12,-0.24,Zportaherramientas,0])
Herramienta2Des=np.array([0.1,-0.21,Zportaherramientas,ang2])
#Angulos para arcos de espacio de trabajo diestro
lim=70*np.pi/180

#Valores de ángulo de cierre del gripper
gripClose=-100*np.pi/180
gripOpen=0

#Radios de espacio de trabajo mínimo y máximo
LimitMin=0.18
LimitMax=0.3

#Posiciones físicas del arco menor y mayor
LimitMin1=np.array([[LimitMin*np.cos(lim),LimitMin*np.sin(lim),Zseguridad,0],[LimitMin*np.cos(lim),LimitMin*np.sin(lim),Zpiso1,0]])
LimitMin2=np.array([[LimitMin*np.cos(-lim),LimitMin*np.sin(-lim),Zpiso1,0],[LimitMin*np.cos(-lim),LimitMin*np.sin(-lim),Zseguridad,0]])
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

        print("Laboratorio 5 de Robótica")

        #Definir los límites de torques (se dejan en el máximo)
        Torques=[1023,1023,1023,1023,1023]
        for i in range(5):    
            jointCommand('', (i+1), 'Torque_Limit', Torques[i], 0)

        #Realizar ida al home
        Mover(HomeP,1,gripOpen)
        TieneTool=0
        Select=0

        while(Select!=2):
            PrintOpciones()
            Select=int(input())
            if Select==1:
                if TieneTool==0: 

                    # Monta herramienta
                    print("Iniciando rutina")
                    StartT = time.time()
                    Mover(Herramienta1,0.3,gripOpen)
                    Mover(Herramienta2,0.5,gripOpen)
                    input()
                    print("Apretar gripper")
                    Mover(Herramienta2,0.5,gripClose)
                    Mover(Herramienta1,1,gripClose)
                    Mover(HomeP,1,gripClose)
                    EndT = time.time()
                    Tiempo=EndT-StartT
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)

                    #Dibuja limites
                    StartT = time.time()                    
                    Limites=[LimitMin1[0,:],LimitMin1[1,:],LimitMin2[0,:],LimitMin2[1,:],LimitMax1[0,:],LimitMax1[1,:],LimitMax2[0,:],LimitMax2[1,:],LimitMin1[0,:],HomeP]
                    timeArray=[1.5,0.5,0.5,0.5,1,2,1.5,2,0.5,1]
                    for i in range(len(Limites)):
                        Mover(Limites[i],timeArray[i],gripClose)
                    Mover(HomeP,1.5,gripClose) #Volviendo al home
                    EndT = time.time()
                    Tiempo=EndT-StartT
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)

                    #Iniciales Nombres
                    StartT = time.time()
                    timeArray=[1.5,1.5,1.5,0.5,0.5,0.5,1,1,1.5,0.5,0.5,0.5,0.5,1,1]
                    for i in range(7):
                        Mover(PuntosC[i,:],timeArray[i],gripClose)
                    time.sleep(1)
                    for i in range(7):
                        Mover(PuntosJ[i,:],timeArray[i],gripClose)
                    for i in range(9):
                        Mover(PuntosD[i,:],timeArray[i],gripClose)
                    Mover(HomeP,1.5,gripClose)
                    EndT = time.time()
                    Tiempo=EndT-StartT
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    StartT = time.time()
                    
                    #Figura libre
                    StartT = time.time()
                    timeArray=[1.5,1.5,1.5,1.5,1.5]
                    for i in range(5):
                        Mover(Puntosojo1[i,:],timeArray[i],gripClose)
                    for i in range(5):
                        Mover(Puntosojo2[i,:],timeArray[i],gripClose)
                    N=25 #Se realizan 25 puntos para la boca
                    Rads=np.linspace(0,np.pi,N)
                    ZPuntos=np.ones(N)*(Zpiso)
                    angPuntos=np.ones(N)*ang2
                    t=0.2
                    timeArray=np.ones(N)*t
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

                    PosIni=[0.2,0,Zseguridad2,ang2]
                    Mover(PosIni,1.5,gripClose)         
                    for i in range(N):
                        Mover(PuntosCirc[i,:],timeArray[i],gripClose)
                    Mover(PosIni,1.5,gripClose)
                    for i in range(N):
                        Mover(PuntosCirc2[i,:],timeArray[i],gripClose)
                    EndT = time.time()
                    Tiempo=EndT-StartT
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)


                    #Desmonte
                    Mover(HomeP,2,gripClose)
                    StartT = time.time()
                    Mover(Herramienta1,0.3,gripClose)
                    Mover(Herramienta2Des,0.5,gripClose)
                    input()
                    print("Apretar gripper")
                    Mover(Herramienta2Des,0.5,gripOpen)
                    Mover(Herramienta1,1,gripOpen)
                    Mover(HomeP,1,gripOpen)
                    EndT = time.time()
                    Tiempo=EndT-StartT
                    print("\ntiempo de ejecucion: %.2f s" % Tiempo)
                    TieneTool=0
                else: 
                    print("La herramienta ya está cargada")
                
            
                
            elif Select==2:
                print("Se Finalizará el programa")
            
            else:
                print("Opción no válida. Saliendo.")
                break
        

    except rospy.ROSInterruptException:
        pass