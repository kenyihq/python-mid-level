def read():
    # Leemos archivo que  contiene solo numeros
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [int(line) for line in file]
    print(numbers)
    
def write():
    # Guardamos esta lista en un txt
    names = ["Kenyi", "Julberht", "Hancco", "Quispe"]
    with open("wirte.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(f"{name}\n")

def run():
    write()

if __name__ == '__main__':
    run()