diccionario = {
    "Nombre" : 'Ruben',
    "Apellido" : 'Álvarez',
    "Edad" : 18    
}

claves = diccionario.keys()
print(claves)

#obteniendo un elemento con get() y si no encuentra nada, no da error el programa continua
valores = diccionario.get("Nombre")
print(valores)

#Eliminando diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("Apellido")
print(diccionario)

#Obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


print(diccionario)