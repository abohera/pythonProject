def main():
# La variable inicio es un número entero introducido por el usuario, la cual marca el principio del intervalo
   inicio = int(input("Introduce el número donde empieza el intervalo: "))
# La variable final es un número entero introducido por el usuario, la cual marca el final del intervalo
   final = int(input("Introduce el número donde acaba el intervalo: "))
# El primer for sirve para delimitar el intervalo desde la variable inicio a la variable final
   for x in range(inicio, final + 1):
       primos = True
# El segundo for divide cada valor dentro del intervalo y si el resultado es 0 no mostrara el valor ya que se trata de un número no primo
       for j in range(2,11):
           if x == j:
               break
           elif x%j == 0:
               primos = False
           else:
               continue
       if primos == True:
# Muestra los valores primos por pantalla
           print(" ",x, end="")

if __name__ == "__main__":
   main()