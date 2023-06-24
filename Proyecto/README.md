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

El objetivo del proyecto es diseñar e implementar rutinas en el robot ABB IRB 140 con el fin de generar un proceso de *Pick & Place*.
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

El punto de alistamiento es un punto intermedio donde se coloca el balde proveniente de la banda transportadora. Además, es el lugar donde la ventosa deposita las piezas tomadas de la estantería.

La ubicación seleccionada para el punto de alistamiento se encuentra en el punto medio entre la banda transportadora, ubicada a la derecha del robot, y la estantería, situada a la izquierda del robot. Desde la perspectiva del robot, el punto de aislamiento está en la parte frontal.

Es importante destacar que este punto se encuentra dentro de los límites articulares del robot, lo que significa que se espera que el robot pueda ejecutar los movimientos y rutinas solicitadas sin dificultades significativas.

Con el objetivo de asegurar un movimiento sencillo del robot y mantenerlo dentro de sus límites articulares, se ha diseñado cuidadosamente la ubicación y los procesos en el punto de alistamiento. Como se puede observar en la imagen, el robot no excede sus límites articulares, lo que facilita la ejecución de las acciones solicitadas.


<h2>
 5.Desarrollo e Implementación en RobotStudio
</h2>

Dentro del software RobotStudio se hace uso del robot ABB IRB 140 con su respectivo controlador, se importan los elementos modelados y se acomodan en el espacio de acuerdo a las medidas realizadas.

Para tener referencia física de los dispositivos que se implementan, se usará el robot 1 del LabSir, en el cual la banda transportadora se sitúa al  lado derecho del robot viéndolo desde su posición de home.

En el entorno de Home de  RobotStudio se generan 3  workobjects, asociados al balde en la banda transportadora, al punto de alistamiento y la estantería respectivamente.

A partir de lo anterior, se ajustan  los elementos en cada parte y se ordenan los modelados según sea el caso.
Para la estantería se realiza en un solo modelo incluyendo las piezas ubicadas en la estantería para mayor facilidad en su manejo. Referente al porta herramienta, se importa el modelo y se asigna como herramienta con la opción de Create tool, en este entorno se crea la herramienta y ahí mismo se ajustan los TCP de la misma, uno para el gancho y otro para la ventosa.En el caso del gancho, su TCP se estima en un punto del mismo donde se asegure que pueda tomar y dejar el balde sin problema. Una vez creada la herramienta se asocia al robot y esta queda configurada para su uso.

<h3>
 Lógica y Programación.
</h3>

La solución planteada para esta implementación consiste en construir 3 WorkObjects (balde, punto de aislamiento y  estantería) desde los cuales se definirán los targets con el fin de simplificar el uso de los mismos.

El origen de cada WorkObject se ubica de tal manera que el sistema se modele lo más cercano posible a la disposición real de los elementos en el laboratorio. 

Para la banda transportadora su origen se ubica en el punto de sujeción del balde y de igual forma para el punto de alistamiento.
Cada workobject tiene un estado estacionario, correspondiente a un target donde el robot se moverá de manera inicial y final, esto con el objetivo de facilitar las rutinas que lo involucran.

La creación de las caminos o path, se hacen en función de cada WorkObject .A continuación se hace una breve descripción del método o ruta de decisión para generar los paths de cada WorkObject. 
* **Balde en la banda transportadora :**  Se hace uso del TCP del gancho. De manera inicial, se hacen 2 caminos, uno para tomar el balde y otro para dejarlo; cada uno consta de 5 targets,en el caso de tomar el balde se generan tarjeta movimiento al punto de estado estacionario - aproximación por un costado al balde -  sujeción del balde - levantamiento el balde - retornar el balde al estado estacionario.
  De manera similar funciona el segundo path para dejar el balde, siguiendo el siguiente orden : levantamiento del balde -  movimiento de bajada del balde - descargue del balde - salida de la herramienta por un costado - retornar al estado estacionario.

* 



<h2>
 6.Implementación en el brazo ABB IRB 140
</h2>
