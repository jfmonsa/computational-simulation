import numpy as np


# ------------------ Generación de números aleatorios ------------------
# np.random.rand(n): Genera un array de n números aleatorios uniformes en el rango [0,1)
# Generar 100 números aleatorios uniformes entre 0 y 1
random_numbers = np.random.rand(100)

# np.random.randint(low, high, size=n): Genera nn enteros aleatorios entre low (incluido) y high (excluido).
# Generar 10 enteros entre 1 y 6 simulando un dado
dice_rolls = np.random.randint(1, 7, size=10)

# np.random.normal(mean, std, size=n): Genera nn números con una distribución normal de media mean y desviación estándar std
# Generar 100 números con distribución normal
normal_numbers = np.random.normal(0, 1, size=100)


# np.random.choice(array, size=n, p=probabilities): Selecciona aleatoriamente nn elementos de un array dado, con probabilidades específicas
np.random.choice([1, 2, 3, 4, 5], size=10, p=[0.1, 0.1, 0.1, 0.1, 0.6])



# ------------------ Operaciones de arrays ------------------
# Crear un array y realizar operaciones
array = np.array([1, 2, 3, 4])
result = array * 2  # Multiplicar cada elemento por 2

# Cálculo rápido de sumas, promedios y desviación estánd
# Calcular promedio y suma
mean = np.mean(array)
total = np.sum(array)

# np.where(condition, x, y): Devuelve un array con valores de x donde la condición es verdadera y y donde es falsa.
# np.linspace(start, stop, num=n): Genera nn valores equidistantes entre start y stop


# ------------------ Operaciones geometricas ------------------
# np.sqrt(array): Raíz cuadrada de cada elemento.
# np.sin(array), np.cos(array), np.exp(array): Funciones


# ------------------ Matplotlib ------------------
# plt.plot(x, y): Dibuja un gráfico de línea conectando los puntos (x,y)(x,y).
# plt.scatter(x, y): Crea un gráfico de dispersión con puntos individuales.
# plt.bar(x, height): Crea un gráfico de barras.
# plt.hist(data, bins=n): Crea un histograma con nn bins.

import matplotlib.pyplot as plt
import numpy as np

# Generar datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Graficar
plt.plot(x, y, label="Seno de x")
plt.title("Gráfico de Seno")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()

# configuración del gráfico
'''
plt.title("Título"): Añade un título al gráfico.
plt.xlabel("Etiqueta eje x"), plt.ylabel("Etiqueta eje y"): Etiquetas de los ejes.
plt.legend(): Muestra la leyenda del gráfico.
plt.grid(True): Activa las líneas de la cuadrícula.
plt.xlim(start, stop), plt.ylim(start, stop): Establece los límites de los ejes.


plt.subplot(rows, cols, index): Divide la ventana en una cuadrícula de rows×colsrows×cols y selecciona el índice del gráfico actual.
plt.subplots(): Crea una figura con múltiples subgráficos y devuelve los ejes.
'''

# Crear subgráficos
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(0, 10, 100)
y1, y2 = np.sin(x), np.cos(x)

# Gráfico 1
axs[0, 0].plot(x, y1)
axs[0, 0].set_title("Seno de x")

# Gráfico 2
axs[0, 1].plot(x, y2)
axs[0, 1].set_title("Coseno de x")

# Mostrar
plt.tight_layout()
plt.show()
