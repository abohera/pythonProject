NOTAS=15

def main():
# Variable que cuenta el número de aprobados
    countaprob = 0
# Variable que cuenta el número de suspensos
    countsuspe = 0
# Variable que almacena las notas aprobadas sumando una con una
    notaprob = 0
# Variable que almacena las notas suspensas sumando una con una
    notsuspe = 0
# Estructura de repetición donde repite la acción hasta la constante NOTAS que tiene un valor de 15
    for i in range(NOTAS):
        nota = int(input("Introduce una nota: "))
# Valida que la nota sea del 0 al 10 y si es así, hace que el usuario vuelva a introducir la nota
        while nota < 0 or nota > 10:
            nota = int(input("Introduce una nota del 0 al 10: "))
# Almacena las notas aprobadas sumando una con una y contando el número de aprobados
        if nota > 5:
            notaprob += nota
            countaprob += 1
# Almacena las notas suspensas sumando una con una y contando el número de suspensos
        else:
            notsuspe += nota
            countsuspe += 1
# Calcula la media de aprobados
    mediaaprob = notaprob/countaprob
# Calcula la media de suspensos
    mediasuspe = notsuspe/countsuspe
# Printea por pantalla el resultado obtenido, en el formato indicado
    print(("\nLa media de aprobados es: %.2f") % (mediaaprob))
    print(("La media de suspensos es: %.2f") % (mediasuspe))
    print(("El número total de aprobados es: %d") % (countaprob))
    print(("El número total de suspensos es: %d") % (countsuspe))

if __name__ == "__main__":
    main()