#Craendo diccionarios con dict()
diccionario = dict(nombre = "Ruben", apellido= "Alvarez")

#Las listas no pueden ser keys y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Dato1", "Dato2"]): "ajajaaj"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys(["Nombre","Apellido","Edad"], 2727)
print(diccionario)