def main():
    aulas_dicc = {}
    registros = int(input("¿Cuantos registros queires introducir?: "))
    for i in range(registros):
        print("\nNúmero de registo %u: " % (i + 1))
        num = int(input("Introduce el número del aula: "))
        while num < 1 or num > 50:
            num = int(input("Introduce un número del 1 al 50: "))
        nom = input("Introduce el nombre del aula: ")
        ip = input("Introduce el rango de direcciones IP del aula: ")
        pc = int(input("Introduce el número de pc's en el aula: "))
        while pc < 1 or pc > 20:
            pc = int(input("Introduce un número del 1 al 20: "))
        aulas_dicc[i] = {
            "Aula" : { "Número": num, "Nombre": nom, "IP": ip, "PC": pc}
        }
    print("\n")
    for x in aulas_dicc.values():
        print(x)

if __name__ == "__main__":
    main()