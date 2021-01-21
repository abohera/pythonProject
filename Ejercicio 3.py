def main():
    num1 = int(input("Introduce un número: ")) #El usuario introducira un número por teclado
    num2 = int(input("Introduce un número: ")) #El usuario introducira un número por teclado
# Escoge el valor más alto de dos números
    A = max(num1, num2)
# Escoge el valor más bajo de dos números
    B = min(num1, num2)
# Calcula el MCD
    while B:
        mcd = B
        B = A % B
        A = mcd

# Mostrara por pantalla el MCD de dos números
    print('El M.C,D de {0} y {1} es {2}'.format(num1, num2, mcd))

if __name__ == "__main__":
   main()