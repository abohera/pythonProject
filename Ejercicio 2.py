# Constante de el total de números que ha de introducir por teclado el usuario
DIV=10

def main():
# Se ha de inicializar la variable sum porque si no dara error
    sum=0
# Este for será el que pida al usuario 10 números decimales y los guardara en la variable sum sumando uno tras otro
    for x in range(10):
       number = float(input("Introduce un número decimal: "))
       sum += number
# La division entre el total de la suma de los números introducidos y el total de números introducidos se guardara en la variable total
    total=sum%DIV
# Mostrara la media de los números introducidos
    print("La media de los números introducidos es: %.2f" % total)
   
if __name__ == "__main__":
   main()