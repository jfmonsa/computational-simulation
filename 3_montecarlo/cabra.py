import random

'''
Calcular las posibilidades de obtener el premio con cada una
de las siguientes estrategias:
a. Si el jugador cambia de puerta.
b. Si el jugador no cambia de puerta.
'''
NUMBER_OF_ITERATIONS = 10_0000

number_of_wins_changing = 0
number_of_wins_not_changing = 0

for i in range(NUMBER_OF_ITERATIONS):
    # 0 = loss, 1 = win
    doors = [0, 0, 0]
    #seleccionamos una puerta al azar para poner el carro
    doors[random.randint(0, 2)] = 1

    # open random door (cabra)
    door = random.randint(0, 2)
    
    # show random door (cabra)
    for i in range(3):
        if i != door and doors[i] == 0:
            puerta_cabra = i
            break
    #si el usuario decide cambiar de puerta
    for i in range(3):
        if i != door and i != puerta_cabra:
            door = i
            break
    #mostrar el resultado
    if doors[door] == 1:
        number_of_wins_changing += 1
    else:
        number_of_wins_not_changing += 1
        
        
              
print("Gano cambiando de puerta:", number_of_wins_changing, "veces")
print("Gano sin cambiar de puerta:", number_of_wins_not_changing, "veces")
print("Probabilidad de ganar cambiando de puerta:", number_of_wins_changing/NUMBER_OF_ITERATIONS)
print("Probabilidad de ganar sin cambiar de puerta:", number_of_wins_not_changing/NUMBER_OF_ITERATIONS)
