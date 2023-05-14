import sys
from cmath import pi
import numpy as np
import rospy
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand

# Obtén la entrada del argumento de línea de comandos
entrada = int(sys.argv[1])


#Arreglo de torques
Torq=[500,400,400,400,300]


#Ángulos deseados
Deg1=[0,0,0,0,0]
Deg2=[40, 23, 42, 40, 0]
Deg3=[72,-72, 125, -92, -23]
Deg4=[-88, 48, -10, -43, 0]
Deg5=[ -41, -69, 86, -97, 0]

#Valores análogos de las posiciones. Se obtuvieron desde dynamixel_wizard
Ana1=[512,526,226,520,264]
Ana2=[651,598,368,656,264]
Ana3=[758,279,650,835,186]
Ana4=[214,682,190,373,264]
Ana5=[372,286,521,190,264]



#Obtener el número del usuario
pose =entrada


#Arreglo de las poses
anaArray=[Ana1,Ana2,Ana3,Ana4,Ana5]
degArray=[Deg1,Deg2,Deg3,Deg4,Deg5]

#Asigna qué pose se va a ejecutar.
anaPose=anaArray[pose-1]
#degPose=degArray[pose-1]
#Un arreglo en ceros donde se almacenarán las posiciones de los ángulos reales.
realPose =[0,0,0,0,0]




#Función que cambia valores de registros de los motores del Pincher.
def jointCommand(command, id_num, addr_name, value, time):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(exc)

#Función callback que se llama en el listener. Cambia la variable global de la posición de los ángulos de los motores.
#Se realiza el ajuste a grados y a la posición home que se estableció
def callback(data):
    global realPose
    realPose=np.multiply(data.position,180/pi)
    realPose[2]=realPose[2]-90

#Función que genera el subscriber para obtener los estados de las articulaciones
def listener():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState,callback)



#Imprime la posición real de los ángulos de los motores.
def printReal(real):
    print('\nÁngulos reales:\n')
    for i in range (len(real)):
        print(f'{str(i + 1)}: ' + "%.2f" % real[i] +'\n' )

#Rutina de movimiento con puntos intermedios. Uno define el número de movimientos N para llegar a un punto.
#Se ejecuta en un ciclo for hasta llegar al punto final.
def Moving(j,Goal,Actual):
    N=5
    delta=((Goal-Actual)/N)
    for i in range(N):
        jointCommand('', (j+1), 'Goal_Position', int(Actual+delta*(i+1)), 0.5)
        time.sleep(0.1)



#Main
if __name__ == '__main__':
    try:
        #Activar el subscriber.
        listener()

        #Definir los límites de torque de los motores.
        for i in range(5):    
            jointCommand('', (i+1), 'Torque_Limit', Torq[i], 0)
            
        #Rutina para ir al home.
        for i in range(5):
            jointCommand('', (i+1), 'Goal_Position', Ana1[i], 1)
            #print('Moviento eslabon: '+str(i+1)+'\n')
            time.sleep(0.5)
        
        #Realizar la rutina de movimiento.
        for i in range(5):
            Moving((4-i),anaPose[4-i],Ana1[4-i])

        #Imprimir la posición deseada respecto a la teórica.
        printReal(realPose)
    except rospy.ROSInterruptException:
        pass



