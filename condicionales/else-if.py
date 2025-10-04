ingreso_mensual = 22000
gasto_mensual = 40000
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas con perdidas de", abs(ingreso_mensual - gasto_mensual) , "euros")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien economicamente")
    else:
        print("Estas gastando demasiado")
    

elif ingreso_mensual > 1000:
    print("Estas bien economicamente en latinoamerica")
    
else:
    ("Eres pobre")