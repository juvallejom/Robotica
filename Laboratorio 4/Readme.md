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

Se definen las longitudes de la siguiente manera :

*L1:


Como se observa, se calculan unas distancias L1, L2, L3 y L4, se miden por medio de un calibrador al pincher directamente y se obtienen los siguientes valores (en mm):
L1: 134.2
L2: 105.2
L3: 105.2
L4: 67.5


