import itertools
'''
Escriba un código en Python para determinar los elementos de un evento si debe cumplir la
condición que la suma de los puntos en dos lanzamientos de un dado no sea mayor que 7.

El resultado de la ejecución de este código es: {(2 , 4), (1, 2), (2, 1), (1, 5), (3, 1), (4 , 1), (1, 1), (5, 1),
(4, 2), (1, 4), (2 , 3), (3, 3), (2, 2), (3, 2), (1, 3)}
'''

def solucion():
    posibles = list(itertools.product(range(1,7), repeat=2))
    resultado = {combinacion for combinacion in posibles  if combinacion[0] + combinacion[1] < 7}
    print(f"El resultado de la ejecución de este código es: {resultado}")

if __name__ == "__main__":
    solucion()