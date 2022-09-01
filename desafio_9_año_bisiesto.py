def año_bisiesto(x):
    if x >= 100:
        if x >= 400:
            if x % 400 == 0:
                return("es bisiesto")
            elif x % 100 != 0 :
                    if x % 4 == 0:
                        return("es bisiesto")
                    elif x % 4 != 0:
                        return("no es bisiesto")
            else:
                 return("no es bisiesto")       
        else:
            if x % 100 != 0 : 
                if x % 4 == 0:
                        return("es bisiesto")   
            else:
                 return("no es bisiesto")      
    elif x % 4 == 0:
        return("es bisiesto")
    elif x % 4 != 0:
        return("no es bisiesto")
    else:
        return("no corresponde a numero valido")    
    
    
print("Ingresar año: ")
año = int(input())
print(f"El año {año} {año_bisiesto(año)}.")