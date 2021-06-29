def try_except_raise(): 
    try:       
        num = int(input('Ingrese un número: '))
        if num < 0 :
            raise ValueError
        divisor = [i for i in range(1, num + 1) if num % i == 0]
        print(divisor)
    except ValueError:
        print("Solo ingrese números enteros positivos")

def assert_statemet():
    try:       
        num = int(input('Ingrese un número: '))
        assert num > 0, "Solo números enteros positivos"
        divisor = [i for i in range(1, num + 1) if num % i == 0]
        print(divisor)
    except ValueError:
        print("Solo ingrese números enteros positivos")

if __name__ == '__main__':
    assert_statemet() 