seed = int(input(
    "Por favor, ingrese una semilla para la generación de números aleatorios: ")
)
etapas = int(input("Ingrese la cantidad de etapas: "))
print()

len_seed = len(str(seed))
i = 0

while (i < etapas):
    print(f"------ Etapa {i + 1} ------")
    cuadrado = str(seed * seed).zfill(len_seed * 2)
    print(f"Cuadrado de {seed}: {cuadrado}")

    # Para sacar el centro
    pos_inicial = int(abs(len(cuadrado) / 2) - abs(len_seed / 2))

    nuevo_num = int(cuadrado[pos_inicial:(pos_inicial + len_seed)])

    i += 1
    seed = nuevo_num

    print(f"Nuevo número: {nuevo_num}")
    print()
