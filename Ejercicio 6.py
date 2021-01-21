def main():
# El usuario introducira un valor del 1 al 10
    numero = int(input("Introduce un valor del 0 al 10: "))
# While validara si el valor introducido esta entre esos dos numeros, si no pedira de nuevo que vuelva a introducir el valor
    while numero < 0 or numero > 10:
        numero = int(input("Introduce un valor del 0 al 10: "))

if __name__ == "__main__":
    main()