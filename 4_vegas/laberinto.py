import random

# Definir el laberinto como una matriz
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

# Coordenadas de inicio y fin
inicio = (0, 0)
fin = (4, 4)

# Movimientos posibles: derecha, izquierda, abajo, arriba
movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def es_valido(laberinto, camino):
    x, y = inicio
    for dx, dy in camino:
        x += dx
        y += dy
        if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]) or laberinto[x][y] == 0:
            return False
    return (x, y) == fin

def generar_camino_aleatorio():
    camino = []
    while True:
        movimiento = random.choice(movimientos)
        camino.append(movimiento)
        if es_valido(laberinto, camino):
            return camino

def resolver_laberinto():
    while True:
        camino = generar_camino_aleatorio()
        if es_valido(laberinto, camino):
            return camino

# Resolver el laberinto
camino_solucion = resolver_laberinto()
print("Camino encontrado:", camino_solucion)