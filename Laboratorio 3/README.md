# Laboratorio 3 : Robotica de Desarrollo e Introduccion a ROS
<p align="center">
 Cristhian David Sandoval Diaz
</p>
<p align="center">
 Dylan Ortiz Mayorga
</p>
<p align="center">
 Juan Pablo Vallejo Montañez
</p>

## Introducción

El objetivo de esta practica es conocer los conceptos principales de ROS (Robot Operation System) y como enlazar elementos (nodos) implementando lenguajes de programación como Python.

Para afianzar estos conceptos se trabajara con la herramienta *turtle* diseñada para familiarizarse con el funcionamiento y el uso de paquetes dentro de ROS 

## Metodologia 

Para realizar esta actividad introductoria se manejo Python por la facilidad y claridad en la creación de funciones, la posibilidad de construir el código de manera conjunta en la aplicación Visual Code Studio y por la experiencia que se tiene en este lenguaje de programación.

Como primer paso se incializa ROS en una terminal.

```
roscore
```
Y de manera paralela se incia el nodo *turtlesim* en otra terminal.

```
rosrun turtlesim turtlesim_node
```
Para realizar la programación mediante un script en Python es necesario incluir las siguientes librerias en la sección incial del código

```
from queue import Empty
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
import numpy as np

TERMIOS = termios
```
INCLUIR DESCRICPCION DE LAS LIBRERIAS PLISSSSSSSSS

Se implementan las funciones que permiten las siguientes operaciones:

• Se debe mover hacia adelante y hacia atrás con las teclas W y S

• Debe girar en sentido horario y antihorario con las teclas D y A.

• Debe retornar a su posición y orientación centrales con la tecla R

• Debe dar un giro de 180° con la tecla ESPACIO

### Función Key 

DESCRIPCION FUNCION KEY 

```
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c
```


### Función pubVel

### Función Reset

### Función Spin 


Con las funciones definidas se crean las condiciones de accionamiento (entrada de teclado) dentro de la sección *main* del script.

```
if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        while(1):
            teclado = getkey()
            if teclado == b'w': 
               pubVel(1,0,0.1)
            if teclado == b'a': 
               pubVel(0,1,0.1)
            if teclado == b's': 
               pubVel(-1,0,0.1)
            if teclado == b'd': 
               pubVel(0,-1,0.1)
            if teclado == b'r': 
               Reset(5.544445,5.544445,0.000000)
            if teclado == b' ': 
               Spin(0,np.pi)
            if teclado == b'f': 
                break
            
    except rospy.ROSInterruptException:
        pass
```
