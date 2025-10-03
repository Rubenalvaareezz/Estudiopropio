#Creando una lista (se pueden modificar)
lista = ["Soy ruben", "Beatriz", True, 1.85]

#Creando una tupla (No se puede modificar)
tupla = ("Soy ruben", "Beatriz", True, 1.85)

#Esto es válido
print(lista[2])

#Esto no es válido
#print(tupla[2])

#Creando un conjunto (set) (No se accede a elementos por índice, no almacena datos duplicados)
conjunto = {"Soy ruben", "Beatriz", True, 1.85}

#print(conjunto[2]) -> no accede a elementos por índice

#Creando un diccionario (dict)
diccionario = {
    #'Key' : "Value"
    'Nombre' : "Ruben",
    'Novia' : "Beatriz",
    'Tiene hambre' : True,
    'altura' : 1.85
}
print(diccionario["altura"])



