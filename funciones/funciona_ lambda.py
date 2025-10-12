numeros = [1,2,3,4,5,6,7,8,9]

#Creando una función lambda
multiplicacion_por_dos = lambda x : x*2
#print(multiplicacion_por_dos(3))

#creando funcion que diga que es par o no
def es_par(num):
    if num % 2 == 0:
        return True
print(es_par(4))

#Usando filter
#numeros_pares = filter(es_par,numeros)
#print(list(numeros_pares))

#Hacer lo mismo pero con lambda
numeros_pares = filter(lambda numero: numero%2 == 0, numeros)
print(list(numeros_pares))
