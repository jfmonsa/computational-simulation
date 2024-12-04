'''
Usando el método Monte Carlo, escribe un programa en Python que estime el valor de π.
    1. Genera puntos aleatorios en un cuadrado de 2x2 centrado en el origen.
    2. Determina cuántos puntos caen dentro de un círculo de radio 1.
    3. sa la relación entre el área del círculo y el área del cuadrado para estimar π
'''
import numpy as np
import matplotlib.pyplot as plt

# Número de muestras
NUMBER_OF_SAMPLES = 100_000

# Generar puntos aleatorios en el cuadrado [-1, 1] x [-1, 1]
x_points = np.random.uniform(-1, 1, NUMBER_OF_SAMPLES)
y_points = np.random.uniform(-1, 1, NUMBER_OF_SAMPLES)

# Determinar los puntos dentro del círculo (x² + y² <= 1)
distances = x_points**2 + y_points**2
inside_circle = distances <= 1 # & y | en lugar de and y or, (indexación booleana)

# Estimar el valor de π
pi_estimate = 4 * np.sum(inside_circle) / NUMBER_OF_SAMPLES

print("Número de puntos generados:", NUMBER_OF_SAMPLES)
print("Número de puntos dentro del círculo:", np.sum(inside_circle))
print("Valor estimado de π:", pi_estimate)

# Visualización
plt.figure(figsize=(8, 8))
plt.scatter(x_points[inside_circle], y_points[inside_circle], color="blue", s=1, label="Dentro del círculo")
plt.scatter(x_points[~inside_circle], y_points[~inside_circle], color="red", s=1, label="Fuera del círculo")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title(f"Estimación de π usando el método Monte Carlo\nValor estimado de π: {pi_estimate}")
plt.axis("equal")  # Asegura que los ejes tengan la misma escala
plt.show()
