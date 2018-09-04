import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

# Ejemplo del gradiente descendente aplicado a la función y = x^2 + 1
# La ecuación matemática para el gradiente (derivada) es = 2*x

x_inicial = randint(10)
alpha = 0.1
n_iteraciones = 15

iteraciones = []
y = []

x = x_inicial
for i in range(n_iteraciones):
	print('------------------------')
	print('iteración ', str(i+1))

	# Calcular gradiente
	gradiente = 2*x

	# Actualizar "x" usando gradiente descendente
	x = x - alpha*gradiente

	# Almacenar iteración y valor correspondiente
	y.append(x**2 + 1)
	iteraciones.append(i+1)

	# Imprimir resultados
	print('x = ', str(x), ', y = ', str(x**2+1))

plt.subplot(1,2,1)
plt.plot(iteraciones,y)
plt.xlabel('Iteración')
plt.ylabel('y')

X = linspace(-5,5,100)
Y = X**2 + 1
plt.subplot(1,2,2)
plt.plot(X,Y,0.0,1.0,'ro')
plt.xlabel('x')
plt.ylabel('y')

plt.show()