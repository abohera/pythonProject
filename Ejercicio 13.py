def main():
# Variable que almacena el primer número introducido
    num1 = int(input("Introduce un número: "))
# Variable que almacena el segundo número introducido
    num2 = int(input("Introduce un número: "))
# Intercambiando los valores de las dos variables
    num1, num2 = num2, num1
# Muestra los valores de las variables por pantalla
    print(num1)
    print(num2)

if __name__ == "__main__":
    main()