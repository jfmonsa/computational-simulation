'''
Escriba un código para enumerar los elementos del complemento de E = {los multiplos de tres } si el espacio
muestral son los numeros de 1 y 17
'''


def solucion():
    # obtengo los multiplos de 3
    complemento_multiplos_3 = [num for num in range(1,18) if not (num % 3 == 0)]
    print( complemento_multiplos_3)



'''
Escriba un codigo parar enumerar los elementos de la unicon de los eventos E1 = {los multiplos de 3}
y E2={los multiplos de 2} si el espacio muestral son los numeros entre 1 y 10
'''
def solucion2():
    E1 = {num for num in range(1,11) if num % 3 == 0}
    E2 = {num for num in range(1,11) if num % 2 == 0}
    print(f"La union de los eventos es: {E1 | E2}")

if __name__ == "__main__":
    print("----------- Ejercicio 1 ---------------")
    solucion()
    print("----------- Ejercicio 2 ---------------")
    solucion2()