numero = 10
numero += 10 #El += lo que hace es añadir al número que ya teníamos definido el que hay detrás del igual
print(numero)

#Definiendo una variable con CamelCase
nombreCompletoDelUsuario= "ruben"

#Definiendo una variable con snake_case
nombre_Completo_Del_Usuario = "ruben"

#Concatenar con  f-strings
Bienevenida = f"Hola, {nombreCompletoDelUsuario} ¿como estas? " #f es igual fstring y convierte todo en texto
print(Bienevenida)


#Concatenar con +
bienvenida = "Hola, " + nombreCompletoDelUsuario + " ¿Como estás?"
print(bienvenida)


#Operadores de pertenencia (in y not in)

print("ola" in Bienevenida) #Sale true si existe ese trozo en el texto donde lo buscamos, de lo contrario saldría false

print("jorge" not in Bienevenida)# Sale true porque es cierto de que no esta en el texto de bienvendia


#del Bienevenida, elimina datos como la variable bienvenida, pero se tiene que poner debajo de lo que se quiere eliminar



