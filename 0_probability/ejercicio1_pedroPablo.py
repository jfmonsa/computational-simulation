# Ejercicio 1
# Complejidad temporal: O(1)
# Complejidad espacial: O(1)

def pedroPabloJuego():
    print("="*10)
    print("Ejercicio 1")
    # suma dados > 7
    contador_pedro = 0

    # diferencias menores que 2
    contador_pablo = 0

    for x in range(1,7):
        for y in range(1,7):

            if x+y > 7:
                contador_pedro+=1
            
            if abs(x-y) < 2:
                contador_pablo+=1

    print(f"probabilidad pedro P(x)={contador_pedro}/6 -> {contador_pedro/36}")
    print(f"probabilidad pablo P(x)={contador_pablo}/6 -> {contador_pablo/36}")
    print(f"No es un juego equitativo tiene la ventaja {'pedro' if contador_pedro > contador_pablo else "pablo"}")
    print("="*10)

if __name__ == "__main__":
    pedroPabloJuego()

