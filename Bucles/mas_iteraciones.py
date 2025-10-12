frutas = ["banana","manzana","uva","pera","naranja","granada","sandia"]
numeros = [2,4,5,8]
cadena = "Hola soy ruben"
#Evitando que se coma una uva con la sentencia Uva
for fruta in frutas:
    if fruta == "uva":
        continue
    print(f"me voy a comer una {fruta}")
print("-------------------------------")   
#Evitar que el bucle siga ejecutandoseç
for fruta in frutas:
    if fruta == "pera":
        break
    print (f"me voy a comer una {fruta}")
print("---------------------")

#For en un solo codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
print("----------------")

#Recorrer una cadena de texto
for letra in cadena:
    print(letra)