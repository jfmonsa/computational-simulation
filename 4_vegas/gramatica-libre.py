import random

# Definir la gramática libre de contexto
gramatica = {
    'S': [['a', 'S', 'b'], ['a', 'b']],
}

# Función para generar una derivación aleatoria
def generar_derivacion(gramatica, simbolo):
    if simbolo not in gramatica:
        return simbolo
    produccion = random.choice(gramatica[simbolo])
    return ''.join(generar_derivacion(gramatica, s) for s in produccion)

# Función para validar una cadena con la gramática
def validar_cadena(gramatica, cadena, max_intentos=1000):
    for _ in range(max_intentos):
        derivacion = generar_derivacion(gramatica, 'S')
        if derivacion == cadena:
            return True
    return False

# Ejemplo de uso
cadena = 'aab'
resultado = validar_cadena(gramatica, cadena)
print(f"La cadena '{cadena}' {'es válida' if resultado else 'no es válida'} según la gramática.")