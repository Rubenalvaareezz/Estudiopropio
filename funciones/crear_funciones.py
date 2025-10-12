def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "niña"
    elif (sexo == "hombre"):
        adjetivo = "cabezon"
    else:
        adjetivo = "crack"
    print(f"Hola {nombre}, mi {adjetivo} como estas?")
saludar ("Beatriz","MujER")

#Crear una función que me retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
password = crear_contraseña_random(0)
print(password)

