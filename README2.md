# English version
# Fuentes y recursos (sources and resources)

Todo el codigo presentado ha sido desarrollado siguiendo lo presentado en el curso de <a href="http://personal.cimat.mx:8181/~mrivera/cursos/temas_aprendizaje.html" target="_blank"> Aprendizaje Automático <a>
El curso mencionado es una herramienta invaluable para cualquiera interesado en el aprendizaje de máquina.
Las definiciones de los métodos se obtuvieron de las páginas mencionadas en cada sección.


# **Métodos de Gradiente (Gradient Methods)**

Los ejemplos únicamente detallan el funcionamiento de los métodos expuestos en problemas de mínimizacion.
La razón es porque el contenido de este repositorio va orientado más hacia el desarrollo de redes neuronales artificiales.
En estos sistemas los optimizadores se utilizan para reducir el error del modelo a la hora de hacer predicciones (inferencia).

## Descenso por Gradiente de vainilla (Gradient Descent vanilla flavour)
  Imagen de la ecuacion la imagen fue creada utilizando word
  Definicion con cita

### Descenso por Gradiente 2D (Gradient Descent 2D)
    El ejemplo [Descenso por gradiente 2D](https://github.com/uli-wizrd/Gradient_Methods/blob/master/GD_CN2.py) 
    Trata sobre del uso de descenso por gradiente de vanilla en la optimizacion de una funcion multivariable convexa.

### Descenso por gradiente 2D con derivada numerica (Gradient Descent 2D with numerical derivatives)

El ejemplo [Descenso por gradiente 2D](https://github.com/uli-wizrd/Gradient_Methods/blob/master/GD_CN2.py) 
Trata sobre el descenso por gradiente en una funcion que vive en un espacio bidimensional (cuando solo necesitas dos variables para describir tu sistema).

### Descenso por Gradiente 3D (Gradient Descent 3D)
    
El ejemplo [Descenso por gradiente 2D](https://github.com/uli-wizrd/Gradient_Methods/blob/master/GD_CN2.py)
    Trata sobre el uso del descenso por gradiente en una funcion que vive en un espacio tridimensional (Cada eje corresponde a una variable de interes)

## 2.- Descenso por Gradiente Estocastico (Stochastic Gradient Descent)

  
El ejemplo trata sobre el uso del descenso por gradiente estocastico en funciones convexas y no convexas

## 3.- Sumthin

El tercero es un ejemplo del metodo empleado en la optimizacion de una funcion no convexa

## 4.-Sumthin

El cuarto es un ejemplo del metodo empleado en la optimizacion de una funcion no convexa

## 5.-ADAM Optimizador Adaptativo de Momento (Adaptative Moment optimizer) 

El Quinto es un ejemplo de la aplicacion del optimizador ADAM presentado en [cira] para una funcion no convexa

# Comparaciones (Comparatives)

El ejemplo [Descenso por gradiente 2D](https://github.com/uli-wizrd/Gradient_Methods/blob/master/GD_CN2.py).
Es una simulacion de como se comparan el descenso por gradiente, el descenso por gradiente estocastico, x, y y ADAM.
La tarea fue encontrar el minimo de la funcion 3D (funcion).
La funcion de la cual se quiere encontrar el minimo en este caso se conoce como funcion de perdida (loss function).
Esta funcion nos reporta el error de nuestro sistema a la hora de hacer predicciones.
Tambien se le conoce a esta funcion como superficie de perdida (Loss surface).
