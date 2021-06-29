def run():
    squares = []
    for i in range(1, 101):
        if i%3 != 0:
            squares.append(i**2)
    
    print(squares)

    # Arriba la forma convensional, abajo la list comprehensions

    squares3 = [i**2 for i in range(1, 101) if i%3 != 0]

    print(squares3)    

# Reto: Guardar en Squares numeros que no sean divisbles de 3
def challenge():

    squares = []
    square_not3 = []
    for i in range(1, 101):
        squares.append(i**2)
    for j in squares:
        if j%3 != 0:
            square_not3.append(j)
    print(square_not3)

def challenge_comprehensions():
        
    reto = [i for i in range(1, 100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(reto)

if __name__ == '__main__':
    challenge_comprehensions()