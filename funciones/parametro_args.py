#Forma no optima de sumar valores
#def suma(lista):
#   numeros_sumados = 0
#   for numero in lista:
#       numeros_sumados = numeros_sumados+numero0
#    return numeros_sumados
#resultado_numeros_sumados = suma([4,5,6,7])
#print(resultado_numeros_sumados)

#Utilizando el operador * como argumento(*args)
def suma(Nombre, *numeros):
    return f"{Nombre} la suma de tus numeros es : {sum(numeros)}"
resultado = suma("Ruben",4,5,6,7,10)
print(resultado)

#forma optima de sumar valores sin usar *args
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([2,3,4,5,6,10])
print(resultado2)
