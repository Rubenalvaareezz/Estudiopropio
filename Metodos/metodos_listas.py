lista = [270424, True]

#Agregando elementos a una lista
lista.append(2025)

#Agregando elemento a una lista en un indice especifico
lista.insert(2,7) #aparece en el indice 2

#Agregando varios elementos a una lista
lista.extend([2026, 92])
print(len(lista))

#Eliminando un elemento de la lista por su indice (POP)
lista.pop(1) #se pueden poner indices negativos, y esto eliminas desde el final de la lista
print(len(lista))

#Removiendo un elemento de la lista por su valor
lista.remove(92)
print(lista)

#Ordenamos de menor a mayor (si usamos reverse = True lo invierte)
lista.sort(reverse=True)
print(lista)

#Invirtiendo los elementos de una lista
lista.reverse()
print(lista)






#Eliminar toda la lista
#lista.clear()