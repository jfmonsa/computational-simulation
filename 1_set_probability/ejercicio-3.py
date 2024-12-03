'''
Determine el número de formas en las que se puede vestir un joven si
dispone de dos pares de zapatos, dos pantalones y tres camisas.
'''

def solucion():
    n_zapatos = 2
    n_pantalones = 2
    n_camisas = 3
    print(f"El joven se puede vestir de {n_zapatos*n_pantalones*n_camisas} ")

    print("La lista de combinaciones es:")

    for zapato in ["zapato1","zapato2"]:
        for pantalon in ["pantalon1","pantalon2"]:
            for camisa in ["camisa1", "camisa2", "camisa3"]:
                print(f"{zapato} , {pantalon} , {camisa}")

if __name__ == "__main__":
    solucion()