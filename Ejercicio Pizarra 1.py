def main():
    registros = int(input("¿Cuantos registros queires introducir?: "))
    this_aula = list()
    this_nom = list()
    this_ip = list()
    this_pc = list()
    for i in range(registros):
        print("\nNúmero de registo %u: " % (i+1))
        num = int(input("Introduce el número del aula: "))
        this_aula.append(num)
        while this_aula[i] < 1 or this_aula[i] > 50:
            this_aula[i] = int(input("Introduce un número del 1 al 50: "))
        nom = input("Introduce el nombre del aula: ")
        this_nom.append(nom)
        ip = input("Introduce el rango de direcciones IP del aula: ")
        this_ip.append(ip)
        pc = int(input("Introduce el número de pc's en el aula: "))
        this_pc.append(pc)
        while this_pc[i] < 1 or this_pc[i] > 20:
            this_pc[i] = int(input("Introduce un número del 1 al 20: "))
    print("\n")
    print("TABLA AULAS")
    for i in range(registros):
        print(this_aula[i], end=" | ")
        print(this_nom[i], end=" | ")
        print(this_ip[i], end=" | ")
        print(this_pc[i])

if __name__ == "__main__":
    main()