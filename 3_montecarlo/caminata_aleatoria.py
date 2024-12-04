'''
Simula una caminata aleatoria unidimensional con un límite superior UU y un límite inferior LL.

    Un partícula comienza en la posición 00.
    En cada paso, se mueve +1 o -1 con igual probabilidad.
    El proceso termina cuando la partícula alcanza UU o LL.

Pregunta:

    Estima la probabilidad de que la partícula alcance UU antes que LL usando Monte Carlo
'''

import random

def caminata_aleatoria(U, L, num_simulaciones):
    exitos = 0

    for _ in range(num_simulaciones):
        posicion = 0
        while posicion > L and posicion < U:
            paso = random.choice([-1, 1])
            posicion += paso
        if posicion == U:
            exitos += 1

    probabilidad = exitos / num_simulaciones
    return probabilidad

# Parámetros
U = 24  # Límite superior
L = -10  # Límite inferior
NUM_SAMPLES = 10000  # Número de simulaciones

# Estimar la probabilidad
probabilidad = caminata_aleatoria(U, L, NUM_SAMPLES)
print(f"La probabilidad de alcanzar {U} antes que {L} es aproximadamente {probabilidad:.4f}")