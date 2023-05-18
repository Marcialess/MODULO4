# Errores sintacticos

# while True Print("Hola")
# Errores de Ejecucion

dividendo = 100

while True:
    try:
        age = int(input("Into your age: "))
        callable = dividendo / age
        break
    except ValueError:
        print("Must into an value age")  
    except ZeroDivisionError:
        print("You can't divide by zero")

        
