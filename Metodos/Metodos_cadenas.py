cadena1 = "Hola soy Ruben"
cadena2 = "Mi novia es Beatriz"

#Convierte a mayusculas
mayuscula = cadena1.upper()

#Convierte a minusculas
minuscula = cadena1.lower()

#Convierte la primera letra en mayuscula
primera_letra_en_mayuscula = cadena1.capitalize()

#Buscamos una cadena en otra cadena (Busca la posición de la palabra que le ponemos), si no encuentra algo muestra -1
busqueda_find = cadena1.find("Hola")

#Buscamos una cadena en otra cadena (Busca la posición de la palabra que le ponemos), si no encuentra algo da error
busqueda_index= cadena1.index("Hola")

#si es numerico devolvemos True, si no devolvemos False
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos True, si no devolvemos False
es_alfanumerico = cadena1.isalpha()

#Buscamos coincidencias de una cadena en otra cadena, devuelve la cantidad de veces que coincida
buscar_coincidencia = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos que una cadena empiece con otra cadena dada, si es así devuelve True
empieza_con = cadena2.startswith("H")

#Verificamos que una cadena termine con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("n")

#Remplaza un trozo de la cadena dada por otra dada
cadena_nueva = cadena1.replace("Ruben", "Xavi")

#Separa en trozos de la cadena
separar = cadena1.split()
print(separar)