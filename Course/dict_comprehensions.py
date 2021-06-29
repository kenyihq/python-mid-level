from math import sqrt

def run():
    # Reto: Crear un diccionario que las llaves sean del 1 al 100
    # y sus valores su cubo de cada numero
    
    my_dict = {}

    for i in range(1, 101):
        if i%3 != 0:
            my_dict[i] = i**3

    print(my_dict)

    # Arriba la forma convensional, abajo la dictionary comprehensions

    dict_comprehension = {i:i**3 for i in range(1, 101) if i%3 != 0}

    print(dict_comprehension)

def challenge():
    
    # squart = {i:round(i**0.5,2) for i in range(1, 1001)}
    squart = {i:sqrt(i) for i in range(1, 1001)}


    print(squart)


if __name__ == '__main__':
    challenge()