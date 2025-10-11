# Programa que cuenta las letras entre la primera y la segunda 'r'

# Pedir la secuencia de letras al usuario
secuencia = input("Introduce una secuencia de letras: ")

# Buscar la posición de la primera 'r'
primera_r = secuencia.find('r')

# Buscar la posición de la segunda 'r', empezando después de la primera
segunda_r = secuencia.find('r', primera_r + 1)

# Comprobar que hay al menos dos 'r'
if primera_r == -1 or segunda_r == -1:
    print("No hay dos letras 'r' en la secuencia.")
else:
    # Calcular cuántas letras hay entre ambas
    cantidad = segunda_r - primera_r - 1
    print(f"Hay {cantidad} letras entre la primera y la segunda 'r'.")
    