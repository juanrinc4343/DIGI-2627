#Taula de multiplicar 

num_taula = int(input("Introdueix un nombre per saber la seva taula de multiplicar: "))

print("La taula del ", num_taula, " és:")
for num in range(1, 11):
    print(num_taula , " x " , num , "=" , num * num_taula)
