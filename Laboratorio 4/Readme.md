# Laboratorio 4 : Cinemática Directa - Phantom X - ROS
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

El objetivo de esta práctica es implementar los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom
X Pincher y usar tópicos de estado, servicios y comando para todos los Joint Controllers del robot Phantom X Pincher.



## 2. Metodología 

### 2.1 Caracterización del Robot Phantom X Pincher y definición de las poses deseadas.

Inicialmente se identifica la cadena cinemática del robot y se determinan la longitud de los eslabones que la componen.
Con las dimensiones de los eslabones establecidas se define la posición de home, y posteriormente se calcula la matriz Denavit-Hartenberg (DH) teninedo en cuenta los offsets para cada articulación. *Ver Figura 1.* 


FIGURA 1

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


Finalmente se establecen  5 poses deseadas del robot, donde la primera corresponde a la posición de home y las restantes se establecen aleaoteareamente.

Para definir los ángulos de las articualaciones de las poses restantes se toman los valores  de cada una de las 4 articulaciones en la posición de home. Para la quinta articulación (asociada al movimiento del gripper) se definen valores arbitrarios. Los valores de las artiulaciones para cada pose se registran en la *Figura 2*

FIGURA 2

Se usa nuevamente MATLAB para visualizar las poses definidas anteoriormente. Se inicializan los valores de las articulaciones *q* para cada una de las poses.


```
q1 = [0 0 0 0]*pi/180;
q2 = [40 23 42 40]*pi/180;
q3 = [72 -72 125 92]*pi/180;
q4 = [-88 48 -10 -43]*pi/180;
q5 = [-41 -69 86 -97]*pi/180;
```

 Se dibujan las poses por medio de la siguiente sección de código :
 
 ```
figure()
ws = [-300 300 -300 300 -50 500];
Robot1.plot ([0 0 0 0], 'workspace', ws, 'noa','noname')
hold on
trplot (eye(4), 'witdh', 2, 'arrow', 'length', 30)
Robot1.teach(q5) %% Usar el q que se desea de entre las opciones
hold off

```
Usando el comando *robot1.teach* se puede cambiar entre una y otra pose. 
Acontinuación se presentan las poses ordenadas desde la pose de home (1) hasta la pose N° 5. 


FIGURA DE LAS POSES






### 2.2 Instalaciones Previas en Ubuntu

Se realiza la instalación de *Dynamizel Wizard* y se descargan los paquetes y librerias necesarios para el manejo de los servomotores.

LINKS

Primero se conecta el pincher y se verifica que el sistema identifique los 5 servomotores usando el siguiente comando:

```
sudo chmod 777 /dev/ttyUSB0
```

Luego de  la identificación de los motores de acuerdo a las configuraciones respectivas en Dynamixel *(usando la opción Scan)*, se  desconecta  y se debe identificar el puerto USB al que pertenece el pincher, por lo general es el USB0, pero se verifica con el siguiente comando.

```
ls /dev/tty*
```

Una vez se tiene identificado el puerto USB,  se crea el espacio de trabajo **catkin**, donde en una carpeta creada llamad **“src”**,  se clona el git del dynamixel one motor.

```
git clone https://github.com/fegonzalez7/dynamixel_one_motor.git
```


Una vez descargado el **dynamixel one motor**, se ubica en una carpeta  catkin workspace, en el cual ubicamos en una carpeta creada y llamada “src”, una vez estando ahí, se hace el catkin_make para crear y establecer el espacio de trabajo, una vez dentro, nos interesa modificar 2 archivos dentro del one motor, el primero es el “basic.yaml” dentro del config, el cual establece el número de articulaciones el robot, este número de articulaciones es el que posee el pincher, es decir, 5 articulaciones, las cuales denominamos respectivamente con su ID, de la siguiente forma:


```
joint_1:
  ID: 1
  Return_Delay_Time: 0
  # CW_Angle_Limit: 0
  # CCW_Angle_Limit: 2047
  # Moving_Speed: 512


joint_2:
  ID: 2
  Return_Delay_Time: 0
 
joint_3:
  ID: 3
  Return_Delay_Time: 0
 
joint_4:
  ID: 4
  Return_Delay_Time: 0
 
joint_5:
  ID: 5
  Return_Delay_Time: 0
```

Después de esto, sencillamente guardamos y nos movemos a la otra modificación, correspondiente a la carpeta “scripts” donde se encontraran 3 archivos que inicialmente nos sirven para entender unas funciones del código python que se explicará más adelante, de momento, se eliminan estos 3 archivos y se dejan unos nuevos, primero el archivo python lab4.py, en donde estará toda la información de movimiento, análisis y lectura de datos e información para la transmisión de datos entre las articulaciones, luego un archivo HMI el cual contendrá la interfaz gráfica para el usuario, y además de esto, para esta misma interfaz, habrán 6 imágenes que se usarán en esta interfaz, correspondientes al logo de la universidad, y cada una de las 5 poses deseadas.

Con esos cambios en el dynamixel one motor quedará listo nuestro laboratorio para su ejecución por medio del launcher del dynamixel one motor, por medio del siguiente comando en el terminal.
roslaunch dynamixel_one_motor one_controller.launch

Una vez ejecutado este comando, funcionará correctamente con las siguientes condiciones, primero se debió haber llamado el setup.bash, con el siguiente comando. ubicados en el workspace.
source devel/setup.bash
Luego, cuando se ejecute, debe estar desconectado el dynamixel. Y por último se observará que ejecutado, se observan las 5 articulaciones con sus 5 ID’s como se indicó anteriormente.




