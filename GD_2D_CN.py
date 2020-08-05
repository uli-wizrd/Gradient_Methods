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

# Se ingresan los datos para realizar los calculos en la funcion
# se crea un rango para derivar la funcion y se ingresa la cantidad de particiones que tendra

tn = int(input("Ingrese el valor negativo en el eje x hasta donde quiere ver su función:\n"))
tp = int(input("Ingrese el valor positivo en el eje x hasta donde quiere ver su función:\n"))
N = int(input("Ingrese la cantidad de particiones del rango especificado:\n"))
h = float(input("Ingrese el tamaño del diferencial que desea emplear:\n"))

xvs = np.linspace(tn, tp, N)


def fprim(x):
    ny = (f(x + h) - f(x)) / h
    return ny


yvs = []


itr = 0
print('{:^20}{:^20}{:^20}'.format('[ Iteración ]', '[ Valores de la derivada ] ', '[ Valores de X a evaluar ]'))
for iii in xvs:
    derivative = fprim(iii)
    yvs.append(derivative)
    itr += 1
    print('          {:^3}                      {:^7}                   {:^7}'.format(itr,round(derivative, 4), round(i, 4)))
fyvs = []
for iii in xvs:
    function = f(iii)
    fyvs.append(function)


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
Valorx = []
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
    Valorx.append(xi)
#  Se imprimen los resultados del calculo

#  Se establecen mas condiciones de paro para el bucle

    if gradiente <= tolerancia:
        print("\nSe realizaron:\n"+str(ii)+" Iteraciones")
        print("\nSe ha cumplido con la tolerancia")
        break
    if ii >= 1000:
        print("\nSe han hecho demasiadas iteraciones, por favor, cambie la tasa de aprendizaje o elija otra función")
        break

# impresion de los calculos ejecutados

print("\nHistorial de valores de X:\n")
for vals in Valorx:
    print(vals)

print("\nHistorial de valores Y:\n")
for vals in yor:
    print(vals)

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


fig, ax = plt.subplots(facecolor='whitesmoke')
ax.set_facecolor('floralwhite')
ax.set_title('Función original (dorada) y Derivada de la función (azul)', color='k')
ax.set_xlabel('X', color='mediumseagreen')
ax.set_ylabel('Y', color='brown')
ax.plot(xvs, fyvs, 'goldenrod', linestyle='-')
ax.plot(xvs, yvs, 'blue', linestyle='--')
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()