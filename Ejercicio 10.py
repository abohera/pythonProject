def main():
    # El usuario introducira los segundos por teclado
    segundos = int(input("Introduce el total de segundos: "))
    # Se haran la operaciones correspondientes y mostrará el resultado por pantalla
    dias = segundos // (24 * 60 * 60)
    segundos = segundos % (24 * 60 * 60)
    horas = segundos // (60 * 60)
    segundos = segundos % (60 * 60)
    minutos = segundos // 60
    segundos = segundos % 60
    # Mostrará los segundos introducidos por teclado en formato: Días/Horas/Minutos/Segundos
    print("{} Día/s | {} Hora/s | {} Minuto/s | {} Segundo/s".format(dias, horas, minutos, segundos))

if __name__ == "__main__":
    main()