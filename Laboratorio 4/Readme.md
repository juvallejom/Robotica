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

### 2.1 Caracterización del Robot Phantom X Pincher

Inicialmente se identifica la cadena cinemática del robot y se determinan la longitud de los eslabones que la componen.
Con las dimensiones de los eslabones establecidas se define la posición de home, y posteriormente se calcula la matriz Denavit-Hartenberg (DH) teninedo en cuenta los offsets para cada articulación. *Ver Figura 1.* 

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

### 2.2 



