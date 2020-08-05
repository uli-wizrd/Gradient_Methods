from sympy import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from numpy.random import randint
import numpy as np
import os
import psutil as ps

# Definicion de la condicion para imprimir la funcion de trabajo

init_printing(use_unicode=True)

x, y, z = symbols('x y z')

# Definicion del tamaño del diferencial, conforme sea mas pequeño mas se asemejara a la derivada exacta evaluada

h = 0.0000001

# Definicion de la derivada como un limite multivariable

fxprim = (((x + h)**2 + y**2) - (x**2 + y**2)) / h

fyprim = ((x**2 + (y + h)**2) - (x**2 + y**2)) / h

# Definicion de la funcion

f = x**2 + y**2

print("\nLa función de trabajo es:", f)

print("\nSe comenzará el descenso por gradiente con los siguientes valores aleatorios:")

theta = randint(10)  # valor de prueba inicial de x
print("Theta 0 o (x) = ", theta)
theta1 = randint(10)  # valor de prueba inicial de y
print("Theta 1 o (y) = ", theta1)

alpha = float(input("Ingrese el valor de la tasa de aprendizaje con el que trabajará:\n"))  # Tasa de aprendizaje

# Definicion de constantes y espacios de almacenamiento

iterations = 0
check = 0
precision = 1 / 1000000
printData = True
maxIterations = 1000
ptheta = []
ptheta1 = []
ex = []
ey = []
itr = []
errx = 0
erry = 0
altura = []

while True:

    #  Ok entonces empleando el lenguaje de sympy lo que haremos sera simplemente sustituir el valor de nuestra prueba
    #  En las variables que resulten de nuestra derivada, al ser multivariables se agregara otro .subs
    #  El es el comando en sympy para realizar la sustitucion, despues .evalf evalua la funcion como si los argumentos
    #  En el tipo de dato float

    temptheta = theta - alpha * N(fxprim.subs(x, theta).subs(y, theta1)).evalf()
    temptheta1 = theta1 - alpha * N(fyprim.subs(y, theta1)).subs(x, theta).evalf()

    # si el numero de iteraciones es muy grande, quiza esta divergiendo entonces, se debe detener el bucle

    iterations += 1
    itr.append(iterations)
    errx += pow(theta - temptheta, 2)
    erry += pow(theta1 - temptheta1, 2)
    Errx = 1 / iterations * errx
    Erry = 1 / iterations * erry
    ex.append(Errx)
    ey.append(Erry)
    alt = N(f.subs(x, theta).subs(y, theta1)).evalf()
    altura.append(alt)
    if iterations > maxIterations:
        print("Demasiadas iteraciones. Ajuste el valor de alpha y asegurese de que la función es convexa")
        printData = False
        break

    # Establecimiento de la condicion de paro.
    if abs(temptheta - theta) < precision and abs(temptheta1 - theta1) < precision:
        break

    # Actualizacion de valores

    theta = temptheta
    theta1 = temptheta1

    # registro de valores
    ptheta.append(theta)
    ptheta1.append(theta1)

    # imprimir resultados

if printData:
    print("La función " + str(f) + " converge a un mínimo")
    print("Número de iteraciones:", iterations, sep=" ")
    print("theta0 (x) final =", temptheta, sep=" ")
    print("theta1 (y) final =", temptheta1, sep=" ")
    print("Penultimo valor de theta0  (x) =", theta, sep=" ")
    print("penultimo valor de theta1  (y) =", theta1, sep=" ")

    print('Historial de valores de theta0 (x):\n ')
    for k in ptheta:
        print(k)

    print('Historial de valores de theta1 (y):\n ')
    for j in ptheta1:
        print(j)

    print('Historial de valores de la altura (z):\n ')
    for l in altura:
        print(l)

# Gráficas de la función de trabajo

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)


def fun(a, b):
    zx = pow(a, 2) + pow(b, 2)
    return zx


Z = fun(X, Y)
ax = plt.axes(projection='3d')
ax.set_title('Gráfica de la función Z = X^2 + Y^2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('z')
ax.view_init(20, 30)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()

ax = plt.axes(projection='3d')
ax.set_title('Gradiente descendente')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(20, 20)
ax.contour3D(X, Y, Z, 50, cmap='gray')
pg = ax.scatter3D(ptheta, ptheta1, zs=0, zdir='y', c=ptheta1, cmap='seismic', label='Aproximación')
plt.colorbar(pg)
ax.legend()
plt.show()

# Graficas del error de calculo

fig, ax = plt.subplots(facecolor='whitesmoke')
ax.set_facecolor('floralwhite')
ax.set_title('Comportamiento del error en X', color='k')
ax.set_xlabel('Error en x', color='mediumseagreen')
ax.set_ylabel('Iteraciones', color='brown')
ax.plot(ex, itr, 'darkgray', linestyle='-')  # Grafica principal
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()

fig, ax = plt.subplots(facecolor=('whitesmoke'))
ax.set_facecolor('floralwhite')
ax.set_title('Comportamiento del error en Y', color='k')
ax.set_xlabel('Error en y', color='mediumseagreen')
ax.set_ylabel('Iteraciones', color='brown')
ax.plot(ey, itr, 'royalblue', linestyle='-')  # Grafica principal
plt.grid()
ax.tick_params(labelcolor='k')
plt.show()

# Ahora se imprimiran los resultados del uso de memoria

def memoria_psutil():
    # regresa el uso de memoria en MB
    process = ps.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem


print("La cantidad de memoria utilizada por este programa es:\n"+ str( memoria_psutil()))