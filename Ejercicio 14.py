def main():
# Variable donde el usuario delimita el número de veces que quiere que se le pregunte por un número
    valores = int(input("¿Cuantos valores vas a introducir?: "))
    this_list = list()
    sum = 0
# Estructura de repetición donde repite la acción hasta la variable valores definida por el usuario
    for i in range(valores):
# El usuario introduce un número y se almacena en la variable num
        num = int(input("Introduce un número: "))
# Se modifica la lista this_list con el valor del número introducido
        this_list.append(num)
# Alamacena el total de la suma, sumando los números de uno en uno
        sum += num
# Muestra el total de la suma
    print(("El total de la suma de todos los valores introducidos es: %d") % (sum))

if __name__ == "__main__":
    main()