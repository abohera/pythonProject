# Constante dle número de veces que ha de introducir un número el usuario
NUMEROS = 10

def main():
# Lista principal
    this_list = []
# Lista de valores pares
    list_senar = []
# Lista de valores impares
    list_parells = []
# Variable que cuenta el número de pares que hay
    parell = 0
# Variable que cuenta el número de impares que hay
    senar = 0
# Estructura de repetición donde repite la acción hasta la constante NUMEROS que tiene un valor de 10
    for i in range(NUMEROS):
        num = int(input("Introduce un número: "))
        this_list.append(num)
# Valida que el número introducido sea del 0 al 10 y si es así, hace que el usuario vuelva a introducir el número
        while this_list[i] < 0 or this_list[i] > 10:
            this_list[i] = int(input("Introduce un número del 0 al 10: "))
# Almacena los valores pares en una lista aparte
        if this_list[i] % 2 == 0:
            list_parells.append(this_list[i])
            parell += 1
# Almacena los valores impares en una lista aparte
        else:
            list_senar.append(this_list[i])
            senar += 1
# Printea por pantalla el resultado obtenido, en el formato indicado
    print("Números pares: ")
    for i in range(parell):
        print(list_parells[i], end=" ")
    print("\n\nNúmeros impares: ")
    for i in range(senar):
        print(list_senar[i], end=" ")

if __name__ == "__main__":
    main()