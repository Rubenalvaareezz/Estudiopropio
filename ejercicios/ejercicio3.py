#1 Pedir el nombre y la edad de los aumnos que vinierona a clase
#El que mas edad tiene es el profeor, el que menor tiene es el asistente

def obtener_compañeros(cantidad_compañeros):
    compañeros = []
    for i in range(cantidad_compañeros):
        nombre = input(f"Dime tu nombre: ")
        edad = int(input(f"Dime tu edad: "))
        compañero = (nombre,edad)   
        compañeros.append(compañero)
    compañeros.sort(key=lambda x : x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor
asistente,profesor = obtener_compañeros(4) 
print(f"El profesor es {profesor} y el asistente es {asistente}")
    