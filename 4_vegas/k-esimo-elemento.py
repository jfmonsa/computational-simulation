import random

def particionar(lista, izquierda, derecha, pivote_indice):
    pivote_valor = lista[pivote_indice]
    lista[pivote_indice], lista[derecha] = lista[derecha], lista[pivote_indice]
    store_index = izquierda
    for i in range(izquierda, derecha):
        if lista[i] > pivote_valor:
            lista[store_index], lista[i] = lista[i], lista[store_index]
            store_index += 1
    lista[derecha], lista[store_index] = lista[store_index], lista[derecha]
    return store_index

def quickselect(lista, izquierda, derecha, k):
    if izquierda == derecha:
        return lista[izquierda]
    
    pivote_indice = random.randint(izquierda, derecha)
    pivote_indice = particionar(lista, izquierda, derecha, pivote_indice)
    
    if k == pivote_indice:
        return lista[k]
    elif k < pivote_indice:
        return quickselect(lista, izquierda, pivote_indice - 1, k)
    else:
        return quickselect(lista, pivote_indice + 1, derecha, k)

def encontrar_k_esimo_mas_grande(lista, k):
    if k < 1 or k > len(lista):
        raise ValueError("k está fuera del rango de la lista")
    return quickselect(lista, 0, len(lista) - 1, k - 1)

# Ejemplo de uso
lista = [3, 2, 1, 5, 6, 4]
k = 2
resultado = encontrar_k_esimo_mas_grande(lista, k)
print(f"El {k}-ésimo elemento más grande en la lista es: {resultado}")