def funcion4(y):
    global z
    condicion_1 = 4
    condicion_2 = 0
    if y == condicion_2 or y % condicion_1 != condicion_2:
        z = "no es bisiesto"     
    elif y % condicion_1 == condicion_2:
        z = "es bisiesto"


def año_bisiesto(x):
    condicion_1 = 400
    condicion_2 = 100
    if x >= condicion_2:
        if x >= condicion_1:
            if x % condicion_1 == 0:
                return("es bisiesto")
            elif x % condicion_2 != 0 :
                funcion4(x)
                return z
            else:
                 return("no es bisiesto")       
        else:
            if x % condicion_2 != 0 : 
                funcion4(x)
                return z
            else:
                return("no es bisiesto")      
    
    else:
        funcion4(x)
        return z
        
 
while True:
    try:
        año = int(input("Ingresar año: "))
        print(f"El año {año} {año_bisiesto(año)}.")
        break
    except:
        print("Valor ingresado incorrecto.")
        
