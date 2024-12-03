'''
MODELO MATEMATICO

Las llegadas de los autos al parking son calculadas con la siguiente formula:
T_LLEGADAS = -l*ln(R)

l <- promedio de llegadas en nuestro ejercicio sera 20
Ln <- logaritmo natural
R <- numero pseudoaleatorio (lo obtenemos con la SEMILLA = 30)


Los tiempos de servicio son calculados de acuero con la formula
tiempo = TIEMPO_PARKING_MAX - TIEMPO_PARKING_MIN
tiempo_parqueo = TIEMPO_PARKING_MIN + (tiempo*R) # Distribucion uniforme
'''


import random
import math
import simpy

SEMILLA = 30
NUM_ESPACIOS_PARKING = 10
TIEMPO_PARKING_MIN = 15
TIEMPO_PARKING_MAX = 200
T_LLEGADAS = 8 # Llega un auto al parking cada 20 min
TIEMPO_SIMULACION = 600 # minutos que dura la simulación
TOT_CLIENTES = 100


te = 0.0 # tiempo de espera total
dt = 0.0 # duracion de servicio total
fin = 0.0 # minuto en el que finaliza

def parquear(cliente_auto):
    global dt
    R = random.random() # random number
    tiempo = TIEMPO_PARKING_MAX - TIEMPO_PARKING_MIN
    tiempo_parqueo = TIEMPO_PARKING_MIN + (tiempo*R) # Distribucion uniforme
    yield env.timeout(tiempo_parqueo) # deja correr el tiempo n minutos
    print(f"Auto listo a {cliente_auto} en {tiempo_parqueo} minutos")
    dt = dt + tiempo_parqueo # Acumula los tiempos de uso de la i


def cliente (env, cliente_auto, espacios_parking ):
    global te
    global fin
    llega = env.now # Guarda el minuto de llegada del cliente_auto
    print(f"{cliente_auto} llego al parqueadero en minuto {llega}")
    with espacios_parking.request() as request: # Espera turno para parquearse
        yield request # Obtiene turno
        pasa = env.now # Guarda el minuto cuando comienza a parquearse
        espera = pasa - llega # Calcula el tiempo que espero
        te = te + espera # Acumula los tiempos de espera
        print(f"{cliente_auto} se parque en un lugar de parking libre en minuto {pasa} habiendo esperado {espera}")
        yield env.process(parquear(cliente_auto)) # Invoca al proceso parquear
        deja = env.now #Guarda el minuto en que termina el proceso parquear
        print(f"<-- {cliente_auto} deja el parqueadero en minuto {deja}")
        fin = deja # Conserva globalmente el ultimo minuto de la simulación


def principal (env, espacios_parking):
    llegada = 0
    i = 0
    for i in range(TOT_CLIENTES): # Para n clientes autos
        R = random.random()
        llegada = -T_LLEGADAS * math.log(R) # Distribucion exponencial
        yield env.timeout(llegada) # Deja transcurrir un tiempo entreuno y otro
        i += 1
        env.process(cliente(env, 'Cliente %d' % i, espacios_parking))
        

print ("------------------- Bienvenido Simulación parqueadero ------------------")
random.seed(SEMILLA) # Cualquier valor
env = simpy.Environment() # Crea el objeto entorno de simulación
espacios_parking = simpy.Resource(env, NUM_ESPACIOS_PARKING) #Crea los recursos (lugares libres en el parquing)
env.process(principal(env, espacios_parking)) #Invoca el proceso principal
env.run() #Inicia la simulación



print ("\n---------------------------------------------------------------------")
print ("\nIndicadores obtenidos: ")
lpc = te / fin
print ("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_CLIENTES
print ("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_ESPACIOS_PARKING
print ("Uso promedio de la instalacion = %.2f" % upi)
print ("\n---------------------------------------------------------------------")