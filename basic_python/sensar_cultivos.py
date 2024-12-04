def generarPlantacion(dimension):
    M, N = dimension
    plantacion = []
    for i in range(M):
        fila = []
        for j in range(N):
            posicion = (i, j)
            cultivos = sensarCultivos(posicion)
            fila.append(cultivos)
        plantacion.append(fila)
    return plantacion


def analizarDensidad(plantacion, limite=4):
    M = len(plantacion)
    N = len(plantacion[0])
    densidad = []
    for i in range(M):
        fila = []
        for j in range(N):
            if plantacion[i][j] < limite:
                fila.append('BAJO')
            else:
                fila.append('ALTO')
        densidad.append(fila)
    return densidad

def reporteCrecimiento(plantacion, densidad):
    M = len(plantacion)
    N = len(plantacion[0])
    
    # Promedios de los cultivos por surcos
    promedios_surcos = [sum(surco) / N for surco in plantacion]
    
    # Posiciones de las parcelas con mayor número de cultivos en cada surco
    max_parcelas = [surco.index(max(surco)) for surco in plantacion]
    
    # Promedios de cultivos para 'ALTO' y 'BAJO'
    alto_cultivos = []
    bajo_cultivos = []
    
    for i in range(M):
        for j in range(N):
            if densidad[i][j] == 'ALTO':
                alto_cultivos.append(plantacion[i][j])
            else:
                bajo_cultivos.append(plantacion[i][j])
    
    promedio_alto = sum(alto_cultivos) / len(alto_cultivos) if alto_cultivos else 0
    promedio_bajo = sum(bajo_cultivos) / len(bajo_cultivos) if bajo_cultivos else 0
    
    return (promedios_surcos, max_parcelas, [promedio_alto, promedio_bajo])

# Ejemplo de uso
# Supongamos que la función sensarCultivos está definida y devuelve valores de ejemplo
def sensarCultivos(posicion):
    # Esta es una función de ejemplo. En la práctica, esta función estará definida externamente.
    ejemplo_plantacion = [
        [5, 3, 2],
        [1, 4, 8],
        [2, 3, 1]
    ]
    i, j = posicion
    return ejemplo_plantacion[i][j]

dimension = (3, 3)
plantacion = generarPlantacion(dimension)
densidad = analizarDensidad(plantacion)
reporte = reporteCrecimiento(plantacion, densidad)

print("Plantación:", plantacion)
print("Densidad:", densidad)
print("Reporte de Crecimiento:", reporte)