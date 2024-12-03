
import numpy as np
import matplotlib.pyplot as plt

def montecarlo_integral(f, a, b, NUMBER_OF_RECTANGLES=10_000):
    # gen random x values between [a,b], x values to be evaluated in f(x)
    x_values = np.random.uniform(a, b, NUMBER_OF_RECTANGLES)

    sumatory = 0.0

    for x_i in x_values:
        sumatory += f(x_i)

    return (b-a)*(1/float(NUMBER_OF_RECTANGLES))*sumatory

if __name__ == "__main__":

    # test 1
    # integration of x^2 in [0,1]
    f = lambda x: x**2
    a = 0
    b = 1
    NUMBER_OF_TESTS=1_000
    NUMBER_OF_RECTANGLES=10_000

    estimations = []
    for _ in range(NUMBER_OF_TESTS):
        result = montecarlo_integral(f, a, b, NUMBER_OF_RECTANGLES)
        estimations.append(result)

    ACTUAL_VALUE = 1/3 # actual value of integration of x^2 between 0 and 1
    # plot estimations
    plt.hist(estimations, bins=30, color='blue', alpha=0.7, edgecolor='black')

    # plot settings
    plt.title(f"Histograma de estimaciones de la integral con {NUMBER_OF_RECTANGLES} puntos por simulación")
    plt.xlabel(f"Valor estimado de la integral (media de cada test): {np.mean(estimations)} \n valor real de la integral: {ACTUAL_VALUE}")

    plt.ylabel("Frecuencia")
    plt.grid(True)

    plt.show()
