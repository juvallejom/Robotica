<div align="center">
<h1> Laboratorio 5 
 
 Robótica de Desarrollo - Cinemática Inversa Phantom X
</div>
<p align="center">
 Cristhian David Sandoval Diaz
</p>
<p align="center">
 Dylan Ortiz Mayorga
</p>
<p align="center">
 Juan Pablo Vallejo Montañez
</p>

## 1. Introducción

El objetivo de esta práctica es determinar el modelo cinemático inverso del robot Phantom X, generar trayectorias de trabajo para dibujar figuras con el robot y operarlo usando ROS a partir de scripts generados en Python.

## 2. Metodología 
 
### 2.1 Caracterización del robot.
 
 
Inicialmente se identifica la cadena cinemática del robot y se determinan la longitud de los eslabones que la componen.
Con las dimensiones de los eslabones establecidas se define la posición de home, y posteriormente se calcula la matriz Denavit-Hartenberg (DH) teninedo en cuenta los offsets para cada articulación. *Ver Figura 1.* 



<p align="center">
  <img width="60%" align="center" src="Imagenes/DH.png"/>
 </p>
<p align="center">
  <em>Figura 1 : Matriz de Denavit-Hartenberg para el robot Phantom x Pincher en su posición de home</em>
 </p>
 


Se definen las longitudes de los eslabones en milímetros *(mm)* con los siguientes valores :

- L1: 134.2
- L2: 105.2
- L3: 105.2
- L4: 67.5

Se realiza la verificación de la matriz  mediante el toolbox de Peter Corke en MATLAB para la posición de home implementando la siguiente sección de código:

```
L = [134.2 105.2 105.2 67.5];
off = [0 pi/2 -pi/2 0];

Ln1 = Link('revolute', 'd', L(1), 'a', 0, 'alpha', pi/2, 'offset', off(1));
Ln2 = Link('revolute', 'd', 0, 'a', L(2), 'alpha', 0, 'offset',   off(2));
Ln3 = Link('revolute', 'd', 0, 'a', L(3), 'alpha', 0, 'offset',   off(3));
Ln4 = Link('revolute', 'd', 0, 'a', L(4), 'alpha', 0, 'offset',   off(4));

Eslab = [Ln1;Ln2;Ln3;Ln4];
T_tool = eye(4);
Robot1 = SerialLink(Eslab, 'tool', T_tool)

```
 
### 2.2 Planteamiento del Problema
En este laboratorio se desea generar una rutina con el robot Phantom X la cual implemente las siguientes tareas : 
 
 - Cargar la herramienta.
 - Dibujar el espacio de trabajo.
 - Dibujar las inciales de los nombres de los integrantes del grupo *(CJD)*
 - Dibujar una figura de estilo libre.
 - Descargar la herramienta.

 A continuación, presentaremos un repaso rápido de en la generación de cada una de las subrutinas.
 
 #### *Cargar la herramienta*
 
 #### *Dibujo del espacio de trabajo*
 
 #### *Dibujo de las iniciales*
 
 <p align="center">
  <img width="20%" align="center" src="Imagenes/letras.png"/>
 </p>
 
 <p align="center">
  <em>Figura 3 :Concepto incial de los puntos y trayectorias para el trazo de las letras </em>
 </p>
 
 #### *Dibujo de figura en estilo libre*
 
  <p align="center">
  <img width="20%" align="center" src="Imagenes/estilolibre.png"/>
 </p>
 
 <p align="center">
  <em>Figura 4 :Concepto incial de los puntos y trayectorias para el trazo de la figura de estilo libre </em>
 </p>
 
 
 #### *Descargar la herramienta*
 
 ### 2.3 Cinemática Inversa
 
Para realizar el proceso de cinemática inversa, la idea básica es obtener valores del efector final en ciertas posiciones con el fin de definir trayectorias que cumplan con los requisitos propuestos.
Cada punto P asociado a una posición del efector final debe ser descompuesto en coordenadas cartesianas *(x,y)* para organizar los puntos respecto a un sistema de coordenadas que se ubica en la base del robot (preferiblemente en el centro de la primera articulación).
 
 De acuerdo a lo anterior se establece el siguiente sistema de coordenadas : 
 
 
 IMAGEN DEL SISTEMA DE COORDENAS
 
 
En términos de pose, el robot Phantom X cuenta con 4 grados de libertad, de esta manera la definición geométrica de cada una de las articulaciones se definen a  partir de los siguientes diagramas.
 
 
 IMAGENES DE LAS GEMOETRIAS INVERSAS
 
## 3. Implementación en Python.

 Para el código, se hace uso de python y de las herramientas vistas  en el laboratorio 4, por lo que inicialmente se consideran las librerías, y luego inmediatamente se declaran todas las funciones a usar.
 
### a) Funciones de Comunicación
 
 ```
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
 ```
 
A partir del comando Goal_Position, se logra mover los motores por medio de una actualización de registro.

 De la misma manera, la función joint_Publisher, es la encargada de publicar el valor de las articulaciones para cada uno de los 5 servomotores.
 
 ```
#Función para enviar datos
pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
rospy.init_node('joint_publisher', anonymous=False)
state = JointTrajectory()
state.header.stamp = rospy.Time.now()
state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_4"]
 ```
Al igual que en el laboratorio 4, esta función hace uso del publisher para poder enviar los datos a cada una de las articulaciones.
 
### b) Cinemática Inversa en Python
 
Después de establecer los offset del Home, se define la cinemática inversa de cada una de las 5 articulaciones **q**, de acuerdo a lo obtenido en el método geométrico anteriormente descrito, donde a partir de L1, L2, L3, L4 y las 3 componentes cartesianas del punto P , se define los valores theta de cada una de las articulaciones *q*.
 
Cabe resaltar que la última articulación corresponde gripper y este consiste únicamente es un estado booleano donde se encuentra sosteniendo o no el marcador.

 
 ```
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
   ```
### c) Función Move

Por ultimo, esta función se encarga de usar las funciones iniciales de publisher y movimiento, unido a las cinemáticas encontradas para resumir en una sola función el  movimiento de los servomotores.

  ```
 def Mover(Pos,t,tool):
    q=np.concatenate(((CinInv(Pos[0],Pos[1],Pos[2],Pos[3])+OffsetHomR[0:4]),np.array([tool])), axis=0)
    time.sleep(2*t)
    joint_publisher(q,t)
    time.sleep(2*t)
  ```
## 4. Ejecución y resultados


https://docs.google.com/document/d/1IW1wlN8kBAo6353ksH-8YsHtTfJ6WyQPiX8TjBVO4R8/edit

Se incluyen evidencias del funcionamiento en [Video Laboratorio 5](https://www.youtube.com/watch?v=DuEC59lp24w)
