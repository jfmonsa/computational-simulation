import random

# Función de partición: toma el último elemento como pivote y organiza los demás alrededor de él
def partition(arr, low, high):
    pivot = arr[high]  # Seleccionamos el pivote como el último elemento
    i = low - 1  # Índice de la posición del pivote
    
    for j in range(low, high):  # Iteramos desde low hasta high-1
        if arr[j] < pivot:  # Si el elemento actual es menor que el pivote
            i += 1  # Incrementamos el índice de la posición del pivote
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos los elementos
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Ponemos el pivote en la posición correcta
    return i + 1  # Devolvemos el índice donde se encuentra el pivote

# Función de Quicksort Las Vegas
def quicksort(arr, low, high):
    if low < high:
        # Selección aleatoria del pivote
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Intercambiamos el pivote seleccionado aleatoriamente con el último
        print(f"Pivote seleccionado: {arr[high]} en la posición {pivot_index}, lista: {arr}")
        
        pi = partition(arr, low, high)  # Llamamos a la función de partición
        print(f"Lista después de partición: {arr}")
        
        quicksort(arr, low, pi - 1)  # Recursivamente ordenamos la parte izquierda
        quicksort(arr, pi + 1, high)  # Recursivamente ordenamos la parte derecha

# Lista de prueba
miLista = [34, 93, 19, 58, 12, 28, 95, 37, 23, 80, 57, 82, 55, 48, 21, 39, 53, 65, 30, 32, 84, 64, 44, 68, 36]

# Llamada al algoritmo
print("Lista original:", miLista)
quicksort(miLista, 0, len(miLista) - 1)

# Imprimir la lista ordenada
print("Lista ordenada:", miLista)