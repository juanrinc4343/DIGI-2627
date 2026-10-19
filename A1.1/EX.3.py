print("És el teu nombre parell o senar?")

nombre = int(input("Introdueix un nombre: "))

if nombre % 2 == 0:
    print("El nombre ", nombre, " és parell")
else:
    print("El nombre ", nombre, " és senar")
