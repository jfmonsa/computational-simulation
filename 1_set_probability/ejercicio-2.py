''''
Escriba un código para determinar en qué cuadrante se encuentra un
punto ingresado por teclado.
'''

def solucion(punto):
    x,y = punto
    str_prefix = "El punto esta sobre el "

    if (x>0 and y>0):
        print(str_prefix + "Cuadrante I")
    elif (x>0 and y<0):
        print(str_prefix + "Cuadrante II")
    elif (x<0 and y<0):
        print(str_prefix + "Cuadrante III")
    elif (x<0 and y>0):
        print(str_prefix + "Cuadrante IV")
    elif (x==0 and y!=0):
        print(str_prefix + "El punto esta sobre el eje y")
    elif (x!=0 and y==0):
        print(str_prefix + "El punto esta sobre el eje y")
    else:
        print(str_prefix + "El punto esta sobre el origen")


if __name__ == "__main__":
    x = float(input("Ingrese la coordenada x: ") )
    y = float(input("Ingrese la coordenada y: ") )
    solucion((x, y))