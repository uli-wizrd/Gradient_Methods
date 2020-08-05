import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

print("El siguiente programa resuelve derivadas parciales de las siguiente forma general:\n1: y = i *x^j + c\n")

# se ingresan los valores de los parametros que definen la forma de la ecuacion de trabajo
i = int(input("Ingrese el valor de la constante i:\n:"))
j = int(input("Ingrese el valor de la constante j:\n:"))
C = int(input("Ingrese el valor de la constante c:\n:"))


# Se definen la funcion y la derivada
def f(x):
    z = i * pow(x, j) + C
    return z


print("La funcion que usted ha ingresado es:\n y = "+str(i)+"*x^"+str(j)+"+"+str(C))


def fprim(x):
    z = i * j * pow(x, j - 1)
    return z


# Se ingresa la tasa de aprendizaje y se define el valor aleatorio donde se comenzara
x_inicial = randint(30)


al = float(input("Ingrese la tasa de aprendizaje:\n"))
alpha = al

print('Valor aleatorio inicial:\n' + str(x_inicial))
tolerancia = float(input("Ingrese la tolerancia deseada:\n"))

# Se definen valores iniciales y espacios de guardado

xi = x_inicial
gradiente = fprim(xi)
ii = 0
erx = 0
errx = []
iteraciones = []
yor = []

# Se crea el bucle que aplica el gradiente descendente

while tolerancia < gradiente:  # Se establece una condicion para la ejecucion de operaciones

    ii += 1
    gradiente = fprim(xi)  # Se evalua la derivada
    xi = x_inicial - alpha * gradiente
    fuo = f(xi)  # FUO (FUncion Original) se determinan las alturas que se estan generando en cada iteracion

    erx += pow((x_inicial - xi), 2)  # Se determina el error
    er = 1/ii * erx
    errx.append(er)

    x_inicial = xi  # Se actualizan los valores
    yor.append(fuo)  # Se guardan las alturas determiandas
    iteraciones.append(ii)  # Se guarda el numero de iteracion

#  Se imprimen los resultados del calculo

    print('Valor de X determinado = ', str(xi), ', Valor de Y determinado = ', str(fuo))

#  Se establecen mas condiciones de paro para el bucle

    if gradiente <= tolerancia:
        print("\nSe realizaron:\n"+str(ii)+" Iteraciones")
        print("\nSe ha cumplido con la tolerancia")
        break
    if ii >= 1000:
        print("\nSe han hecho demasiadas iteraciones, por favor, cambie la tasa de aprendizaje o elija otra función")
        break

# Se imprimen las graficas de los resultados del analisis

fig, ax = plt.subplots(facecolor='whitesmoke')
ax.set_facecolor('floralwhite')
ax.set_title('Descenso por Gradiente', color='k')
ax.set_xlabel('Iteraciones', color='mediumseagreen')
ax.set_ylabel(' Valor de Y determinado', color='brown')
ax.plot(iteraciones, yor, 'xkcd:blue', linestyle='--')
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()


fig, ax = plt.subplots(facecolor='whitesmoke')
ax.set_facecolor('floralwhite')
ax.set_title('Evolución del error en X', color='k')
ax.set_xlabel('Iteraciones', color='mediumseagreen')
ax.set_ylabel('Error', color='brown')
ax.plot(iteraciones, errx, color='thistle', linestyle='-')
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()

X = linspace(-5, 5, 100)
Y = f(X)
Yp = fprim(X)
fig, ax = plt.subplots(facecolor='whitesmoke')
ax.set_facecolor('floralwhite')
ax.set_title('Función original (dorada) y Derivada de la función (azul)', color='k')
ax.set_xlabel('X', color='mediumseagreen')
ax.set_ylabel('Y', color='brown')
ax.plot(X, Y, 'goldenrod', linestyle='-')
ax.plot(X, Yp, 'blue', linestyle='--')
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()