# Ejercicio Area bajo la curva
# El área bajo la curva de una función f puede estimarse mediante el método de
# Montecarlo, que consiste en lo siguiente:

# Establecer un rectángulo tal que x Є [a,b]; y Є [0,d], tal que y=f(x)
# d -> altura
# a -> x0
# b -> y0

import math
import random
import matplotlib.pyplot as plt

f = lambda x: x * math.e ** (-x/2)

NUMBER_OF_RANDOM_POINTS = 10000
A = 0 # x0
B = 2 # x1
D = 2 # altura del rectangulo

def gen_random_point():
    x = random.uniform(A + 1e-10,B + 1e-10)
    y = random.uniform(0 + 1e-10,D + 1e-10)
    return (x, y)

def main():
    number_of_points_under_curve = 0
    x_values = []
    y_values = []
    y_values_graph_function = []

    for _ in range(NUMBER_OF_RANDOM_POINTS):
        x , y = gen_random_point()
        x_values.append(x)
        y_values.append(y)
        y_values_graph_function.append(f(x))
        if y < f(x):
            number_of_points_under_curve += 1
    
    print("Número de puntos generados", NUMBER_OF_RANDOM_POINTS)
    print("Número de puntos debajo de la curva", number_of_points_under_curve)
    print("Area bajo la curva " +  str(number_of_points_under_curve/NUMBER_OF_RANDOM_POINTS) + " unidades")
    
    plt.scatter(x_values, y_values,  color="green", label="puntos generados")
    plt.plot(x_values, y_values_graph_function, color="red",  label="y = xe^(-x/2)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Puntos generados y curva `y = xe^(-x/2)`")

    plt.show()


if __name__ == "__main__":
    main()
	
