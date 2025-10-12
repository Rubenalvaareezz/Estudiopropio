diccionario = {
    "Nombre" : 'Ruben',
    "Apellido" : 'Alvarez',
    "Edad" : 18
}

for key in diccionario:
    print(f"la clave es: {key}")



#Aqui obtienes las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La calves del diccionario es: {key} y su valor es {value}")