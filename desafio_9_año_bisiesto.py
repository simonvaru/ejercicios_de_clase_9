def funcion4(y):
    global z
    if y == 0 or y % 4 != 0:
        z = "no es bisiesto"     
    elif y % 4 == 0:
        z = "es bisiesto"


def año_bisiesto(x):
    if x >= 100:
        if x >= 400:
            if x % 400 == 0:
                return("es bisiesto")
            elif x % 100 != 0 :
                funcion4(x)
                return z
            else:
                 return("no es bisiesto")       
        else:
            if x % 100 != 0 : 
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
        
