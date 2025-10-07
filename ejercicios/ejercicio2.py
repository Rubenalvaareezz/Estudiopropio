print("-----------------")
frase = input("Dime una frase: ")
cantidad_palabras = frase.split(" ")
tiempo = len(cantidad_palabras)
numero_palabras = len(cantidad_palabras)
print(f'La persona tardaria {tiempo/2} segundos en decir la frase')
print(f'La persona dijo en la frase un total de {numero_palabras} palabras')

print("---------------")
print(f'Dalto lo diria en {(tiempo/2) / 1.3} segundos')

print("-------------")

if numero_palabras > 120:
    print("No te enroyes tanto brother")

