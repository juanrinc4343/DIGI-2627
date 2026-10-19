#Màxim de tres nombres

print("Posa 3 números: ")
nombre1 = float(input("Introdueix el valor 1: "))
nombre2 = float(input("Introdueix el valor 2: "))
nombre3  = float(input("Introdueix el valor 3: "))


if nombre1 > nombre2 and nombre1 > nombre3:
    print (nombre1)
elif nombre2 > nombre1 and nombre2 > nombre3:
    print (nombre2)
else:
    print(nombre3)