TOTAL=3

def main():
# El usuario introducira un número por teclado
    number_one = int(input("Introduce un número: "))
# El usuario introducira un número por teclado
    number_two = int(input("Introduce un número: "))
# El usuario introducira un número por teclado
    number_three = int(input("Introduce un número: "))
    suma = 0
# El if sirve para comprobar si los valores introducidos son iguales o no
    if number_one == number_two and number_three:
# Si los valores son iguales se hace la suma
       suma = number_one + number_two + number_three
# Y se multiplicara por 3 el resultado de la suma
       suma = suma * TOTAL 
    else:
# Si no son iguales simplemente mostrara el resultado de la suma
        suma = number_one + number_two + number_three
    print("El total es: %u" % suma)
    
if __name__ == "__main__":
    main()