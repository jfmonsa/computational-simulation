import random

def simular_mordida(fila):
    # Cerberus elige al azar uno de los primeros tres de la fila
    mordido = random.choice([0, 1, 2])  # Elegir entre el primero, segundo o tercero
    # El que es mordido se salva, el resto se mueve hacia la izquierda
    if mordido == 0:
        nuevo_fila = [fila[1], fila[2]] + fila[3:]  # El segundo y tercero avanzan
    elif mordido == 1:
        nuevo_fila = [fila[0], fila[2]] + fila[3:]  # El primero y tercero avanzan
    else:
        nuevo_fila = [fila[0], fila[1]] + fila[3:]  # El primero y segundo avanzan
    return nuevo_fila, mordido

def simular_inframundo(fila_inicial, num_simulaciones=10000):
    # Contar cuántas veces cada posición se salva
    salvaciones = [0] * len(fila_inicial)
    
    for _ in range(num_simulaciones):
        fila = fila_inicial[:]
        while len(fila) > 3:  # Mientras haya más de 3 personas en la fila
            fila, mordido = simular_mordida(fila)
        # Al final, registramos si el mordido (que se salvó) estaba en alguna de las primeras 3 posiciones
        salvaciones[mordido] += 1
    
    # Calculamos las probabilidades de salvación desde cada posición
    probabilidades = [salvacion / num_simulaciones for salvacion in salvaciones]
    return probabilidades

def main():
    # Simulamos la fila inicial (puedes ajustarla según tus necesidades)
    fila_inicial = ["Persona 1", "Persona 2", "Persona 3", "Persona 4", "Persona 5", "Persona 6"]
    
    # Realizamos las simulaciones
    probabilidades = simular_inframundo(fila_inicial)

    # Mostramos las probabilidades de salvación para cada persona (posición)
    print("Probabilidades de salvación desde cada posición:")

    bestPos = 0

    # Imprimir las probabilidades de cada posición
    for i, probabilidad in enumerate(probabilidades):
        print(f"Posición {i+1}: {(probabilidad*100):.2f} %")
    
    # Encontrar la posición con la mayor probabilidad
    bestPos = probabilidades.index(max(probabilidades))

    # Imprimir la posición con la mayor probabilidad
    print(f"La posición con más probabilidad de salvación es la {bestPos + 1} con probabilidad de {max(probabilidades) * 100:.2f}%")

if __name__ == "__main__":
    main()