animales = ["gato","perro","loro","cocodrilo"]
numeros = [20,39,94,56,]

for animal in animales:
    print(f"ahora la variable animal es igual a {animal}")
    
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
#Iterar dos listas del mismo tamaño al mismo tiempo.
for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
 
#Forma no opitma de recorrer una lista, para conjuntos esto no sirve
   
for num in range (len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f"El indice de la lista es {indice} y el valor es {valor}")
    
#Usando el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print(f"El bucle actual terminó")
    
#Esto funciona también para tuplas y conjuntos