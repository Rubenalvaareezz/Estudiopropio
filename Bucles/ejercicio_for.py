n = int(input("Dime un numero entero positivo: "))
suma_pares = 0
for i in range(1, n+1):
    if i % 2 == 0:
        suma_pares += i

print("La suma de los números pares hasta", n, "es:", suma_pares)