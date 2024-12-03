'''
Escriba un código en Python para enumerar el evento E = {puntaje menor que 4} a partir de su des cripción
formal en el lanzamiento de un dado

El resultado de la ejecución de este código
'''

def solucion():
    E = {puntaje for puntaje in range(1,7) if puntaje < 4 }
    print(f"El resultado de la ejecución de este código es {E}")

if __name__ == "__main__":
    solucion()