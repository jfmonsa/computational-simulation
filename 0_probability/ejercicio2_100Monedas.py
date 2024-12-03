import random

# Ejercicio 2: Lanzar 100 monedas
def probabilidadLanzar100Monedas():
    print("="*10)
    print("Ejercicio2")
    caras = 0
    sellos = 0

    for i in range(100):
        if random.randint(0,1)==0:
            caras += 1
        else:
            sellos += 1

    print(f"Han salido {caras} caras y {sellos} sellos")
    print("="*10)

if __name__ == "__main__":
    probabilidadLanzar100Monedas()
