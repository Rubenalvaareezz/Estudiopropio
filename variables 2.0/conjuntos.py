#Creando un conjunto con set()
conjunto = set(["dato1" , "dato2"])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1","Dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

#verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)
print(resultado1)
#Tambien se puede hacer con => <=
#rusultado1 = conjunto2 <= conjunto1

resultado2= conjunto1.issuperset(conjunto2)
print(resultado2)
#resultado2 = conjunto1 >= conjunto2
#print(resultado2)