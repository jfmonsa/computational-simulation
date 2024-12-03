import itertools

'''
Escriba un programa que calcule la probabilidad de que el producto de
los puntos de tres lanzamientos de los dados sea menor que 50.
'''

'Solucion 1, mirar la solucion 2'
def solucion():
    eventos_favorables = 0
    eventos_totales = 6*6*6
    
    # contar
    for d1 in range(1,7):
        for d2 in range(1,7):
            for d3 in range(1,7):
                product = d1*d2*d3
                if product < 50:
                    eventos_favorables += 1

    print(f"P(x) = {eventos_favorables}/{eventos_totales} = {eventos_favorables/eventos_totales}")


'Solucion 2 '
def calcular_productos_menores_que_50():
    # Generar todas las combinaciones posibles de dos dados
    dados = list(itertools.product(range(1, 7), repeat=2))
    
    # Calcular todos los productos posibles para un lanzamiento de dos dados
    productos = [dado[0] * dado[1] for dado in dados]
    
    total_combinaciones = 0
    combinaciones_favorables = 0
    
    # Iterar sobre todas las posibles combinaciones de tres lanzamientos
    for lanzamiento1 in productos:
        for lanzamiento2 in productos:
            for lanzamiento3 in productos:
                suma_productos = lanzamiento1 + lanzamiento2 + lanzamiento3
                if suma_productos < 50:
                    combinaciones_favorables += 1
                total_combinaciones += 1
    
    # Calcular la probabilidad
    probabilidad = combinaciones_favorables / total_combinaciones
    print(f"La probabilidad de que la suma de los productos de los puntos de tres lanzamientos de dos dados sea menor que 50 es: P(x) = {combinaciones_favorables} / {total_combinaciones} =  {probabilidad:.4f}")
    return probabilidad

if __name__ == "__main__":
    calcular_productos_menores_que_50()
    #solucion()

                
