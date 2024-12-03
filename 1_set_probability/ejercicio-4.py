'''
Ejemplo 3 . Escriba un código para determinar por enumeración el espacio muestral del lanzamiento triple de un
dado.

El resultado (fragmento) de la ejecución de este código es: {(5 , 1, 6), (5, 3, 3), (5, 4, 2), (2 , 1, 6),
(1, 6, 6), (2, 2, 5), (6 , 6, 4), ...
'''

def solucion():

    posibles_resultados = {1,2,3,4,5,6}
    espacio_muestral = set()

    for d1 in posibles_resultados:
        for d2 in posibles_resultados:
            for d3 in posibles_resultados:
                espacio_muestral.add((d1,d2,d3))

    print(f"El fragmento de la ejecucion de este código es:\n {espacio_muestral}")

if __name__ == "__main__":
    solucion()