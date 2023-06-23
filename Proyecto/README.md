<div align="center">
<h1> Robótica
 
 Proyecto Final
 

</div>
<p align="center">
 Cristhian David Sandoval Diaz
</p>
<p align="center">
 Dylan Ortiz Mayorga
</p>
<p align="center">
 Juan Pablo Vallejo Montañez
</p>**

<h2>
 1.Descripción del Problema
</h2> 

El objetivo del proyecto es diseñar e implementar rutinas en el robot ABB IRB 140 con el fin de generar un proceso de *Pick & Place*-
De manera concisa, el proyecto consiste en realizar una rutina dividida en 3 partes: 
* **Movimiento del Balde :** El robot ABB IRB 140 sujeta un balde desde una banda transportadora con un gancho, y de ahí se transporta a un  punto de alistamiento.
* **Selección de piezas de la estanteria:** Se toman 4 de las 6 piezas ubicadas en la estanteria mediante una ventosa y se ddepositan en el balde en el punto de alistamiento.
* **Transporte Final:** Se sujeta el toma el balde con las 4 piezas y se lleva de regreso a la banda transportadora.




<h2>
 2.Diseño de la Herramienta
</h2>

El portaherramienta se diseñó para ser impresa en 3D con PLA, en este caso se planteó 3 piezas para imprimir debido a que la complejidad de la geometría se  dividio en 3 para  imprimirla de manera correcta. Se idearon 3 partes :
* Sección de anclaje al ABB
* Sujeción ventosa y ventosa
* Sección de cambio de orientación de la ventosa.

<h2>
 3.Diseño y modelado de elementos.
</h2>

Para realiazr la implementación de las rutinas en RobotStudio es necesario tener modelos de los elementos (herramientas,piezas, estanteruas) para incluirlos en el entorno de simulación. A continuación, se detalla el proceso de modelado de cada elemento.

<h3>
 3.1. Estanteria. 
</h3>

El estanteria implementada tiene las siguientes medidas.

IMAGEN MEDIDAS ESTANTERIA 

La estanteria presenta una profundidad de 10 cm. Con estas mediadas se construye un modelado con el software Autodesk Inventor. 

INSERTAR MODELO ESTANTERIA

REFERENCIAR EL MODELADO ACA

INSERTAT IMAGEN PLANO ESTANTERIA 

<h3>
 3.3. Piezas. 
</h3>

La piezas corresponden a las geometrías que toma la ventosa para dejar en el balde. Estas figuras son arbitrarias y se 	realizan 6 modelos distintos.
La única restricción es su tamaño el cual debe ser meayor a la campana de succión de la ventosa para que se pueda sujetar completamente pero debe ingresar al balde sin esfuerzo por lo que hay un tamaño máximo para las piezas.


INSERTAR MODELAADO DE PIEZAS

<h3>
 3.3. Portaherramientas, balde y gancho. 
</h3>

El modelado de la herramienta se toma de su proceso de construccion descrito en la *Sección 2*.
Por otro lado, el modelado del gancho y del balde son incluidos dentro del planteamiento del proyecto.

INCLUIR MODELADO BLADE

INCLUIR MODELADO GANCHO


<h2>
 4.Sección de Alistamiento
</h2>

<h2>
 5.Desarrollo e Implementación en RobotStudio
</h2>

<h2>
 6.Implementación en el brazo ABB IRB 140
</h2>
