# Utilizando los datos indicados para el ejercicio en el correo
SEED = 9731
ITERACIONES = 100
i = 0

while (i < ITERACIONES):
    print(f"------ Iteración #: {i + 1} ------")
    # Si el resultado tiene menos de 8 digitos se añaden ceros a la izquierda
    cuadrado = str(SEED * SEED).zfill(8)
    print(f"Cuadrado de {SEED}: {cuadrado}")

    # Se obtienen los 4 digitos centrales requeridos por el algoritmo
    # 8 es el lenght del cuadrado (numero obtenido)
    pos_inicial = 2
    nuevo_num = int(cuadrado[pos_inicial:(pos_inicial + 4)])

    i += 1
    SEED = nuevo_num

    print(f"Nuevo número: {nuevo_num}")