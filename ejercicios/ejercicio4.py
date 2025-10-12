def es_primo (num):
    for i in range(2, num-1):
        if num%i == 0: return False
    return True

def primo(numero):
    primos=[]
    for i in range (2,numero):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos
resultado = primo(98)
print(resultado)
        
