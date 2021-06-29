print("COMPARAR EDADES")

name1 = input("Nombre de la primeara persona: ")
age1 = int(input("Edad: "))
name2 = input("Nombre de la segunda persona: ")
age2 = int(input("Edad: "))

if age1 > age2:
    print(f"{name1} es mayor que {name2}")
elif age2 > age1:
    print(f"{name2} es mayor que {name1}")
elif age1 == age2:
    print("Ambos tiene la misma edad")
