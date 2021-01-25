def main():
# Numero es la variable que se incrementara del 0 al 10
    numero=0
# La primera estructura de repetición es un for con un rango de la posición 0 a la 11, con lo cual mostrara 10 veces el Titulo "Tabla de multiplicar del 'numero'" en cuestión
    for numero in range(0,11):
        print(("\nTabla de multiplicar del %d") % (numero))
        print("------------")
# La segunda estructura de repetición es un for con el mismo rango que el anterior, pero este se encarga de calcular el resultado de las operaciones y mostrarlas por pantalla
        for i in range(0,11):
            total=i*numero
            print(("%d * %d = %d")%(numero,i,total))

if __name__ == "__main__":
    main()