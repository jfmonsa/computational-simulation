'''
Simula un dado de seis caras sesgado con probabilidades específicas: P(1)=0.1P(1)=0.1, P(2)=0.2P(2)=0.2, P(3)=0.3P(3)=0.3, P(4)=0.1P(4)=0.1, P(5)=0.2P(5)=0.2, P(6)=0.1P(6)=0.1.

    Usa un método Monte Carlo para simular lanzamientos del dado sesgado.
    Realiza N lanzamientos y estima las probabilidades observadas.

Pregunta:

    ¿Cuántos lanzamientos se necesitan para que las probabilidades observadas se acerquen a las esperadas dentro de un 5% de error?
'''

import random

def lanzar_dado_sesgado():
    probabilidades = [0.1, 0.2, 0.3, 0.1, 0.2, 0.1]
    caras = [1, 2, 3, 4, 5, 6]
    return random.choices(caras, probabilidades)[0]

def simular_lanzamientos(N):
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for _ in range(N):
        resultado = lanzar_dado_sesgado()
        resultados[resultado] += 1
    
    probabilidades_observadas = {cara: resultados[cara] / N for cara in resultados}
    return probabilidades_observadas

def calcular_error(probabilidades_observadas, probabilidades_esperadas):
    errores = {cara: abs(probabilidades_observadas[cara] - probabilidades_esperadas[cara]) / probabilidades_esperadas[cara] for cara in probabilidades_esperadas}
    return errores

# Probabilidades esperadas
probabilidades_esperadas = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.1, 5: 0.2, 6: 0.1}

# Simular lanzamientos
N = 10000
probabilidades_observadas = simular_lanzamientos(N)

# Calcular errores
errores = calcular_error(probabilidades_observadas, probabilidades_esperadas)

# Mostrar resultados
print(f"Probabilidades observadas después de {N} lanzamientos:")
for cara in probabilidades_observadas:
    print(f"  P({cara}) = {probabilidades_observadas[cara]:.4f}")

print("\nErrores relativos:")
for cara in errores:
    print(f"  Error relativo en P({cara}) = {errores[cara] * 100:.2f}%")

# Determinar si los errores están dentro del 5%
dentro_del_5_por_ciento = all(error <= 0.05 for error in errores.values())
print(f"\n¿Las probabilidades observadas están dentro del 5% de error esperado? {'Sí' if dentro_del_5_por_ciento else 'No'}")