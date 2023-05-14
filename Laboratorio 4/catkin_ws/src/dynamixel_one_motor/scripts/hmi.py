import tkinter as tk
import os
import subprocess

# Obtén la ruta absoluta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al archivo en la misma carpeta
ruta_otro_archivo = os.path.join(directorio_actual, 'prueba3.py')

def ejecutar_otro_archivo(entrada):

    mostrar_imagen()

    # Ejecuta el otro archivo Python y obtén la salida
    proceso = subprocess.Popen(['python', ruta_otro_archivo, entrada], stdout=subprocess.PIPE)
    salida = proceso.communicate()[0].decode('utf-8')
    
    # Actualiza la salida en la interfaz gráfica
    texto_salida.delete(1.0, tk.END)
    texto_salida.insert(tk.END, salida)


    


# Función para mostrar la imagen y valores según el número ingresado
def mostrar_imagen():
    numero = int(entry_numero.get())

    # Obtener el nombre del archivo de imagen según el número
    nombre_imagen = f"q{numero}.png"

    # Cargar la imagen
    imagen = tk.PhotoImage(file=nombre_imagen)

    # Mostrar la imagen 
    imagen_label.config(image=imagen)
    imagen_label.image = imagen

    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("LAB4")
ventana.geometry("900x600")

# Crear contenedor para la columna izquierda
contenedor_izquierdo = tk.Frame(ventana)
contenedor_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

# Crear contenedor para la columna central
contenedor_central = tk.Frame(ventana)
contenedor_central.pack(side=tk.LEFT, padx=10, pady=10)

# Crear contenedor para la columna derecha
contenedor_derecha = tk.Frame(ventana)
contenedor_derecha.pack(side=tk.LEFT, padx=10, pady=10)


# Crear un logo
logo = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(contenedor_izquierdo, image=logo)
logo_label.pack(pady = 30)

# Crear un texto con los nombres de los integrantes
integrantes_texto = "Integrantes:\n\nCristhian Sandoval       C.C: 1052416059\nDylan Ortiz            C.C: 1000364751\nJuan Pablo Vallejo     C.C: 1000156893"
integrantes_label = tk.Label(contenedor_izquierdo, text=integrantes_texto, justify="left")
integrantes_label.pack(pady = 10)

# Crear contenedor para los elementos de la columna izquierda
contenedor_elementos = tk.Frame(contenedor_izquierdo)
contenedor_elementos.pack(padx=10, pady=10)

# Crear etiqueta y campo de entrada para el número
etiqueta_numero = tk.Label(contenedor_elementos, text="Ingresa la pose que desea del 1 al 5:")
etiqueta_numero.pack()
entry_numero = tk.Entry(contenedor_elementos)
entry_numero.pack()

# Crear botón para mostrar la imagen y los valores reales
boton_mostrar = tk.Button(contenedor_elementos, text="Mover", command=lambda: ejecutar_otro_archivo(entry_numero.get()))
boton_mostrar.pack()


# Crear etiqueta para los valores
valores_label = tk.Label(contenedor_derecha, text="Valores reales")
valores_label.pack()
texto_salida = tk.Text(contenedor_derecha)
texto_salida.pack()

# Crear contenedor para la imagen
contenedor_imagen = tk.Frame(contenedor_central)
contenedor_imagen.pack(padx=10, pady=10)

# Crear label para la imagen
imagen_label = tk.Label(contenedor_imagen)
imagen_label.pack()

# Ejecutar la interfaz gráfica
ventana.mainloop()
