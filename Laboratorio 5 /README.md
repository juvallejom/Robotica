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
 
 

 
## 3. Ejecución y resultados


https://docs.google.com/document/d/1IW1wlN8kBAo6353ksH-8YsHtTfJ6WyQPiX8TjBVO4R8/edit

Se incluyen evidencias del funcionamiento en [Video Laboratorio 5](https://www.youtube.com/watch?v=DuEC59lp24w)
