def main():
    segundos= int(input("Introduce el total de segundos: "))
    dias= segundos // (24 * 60 * 60)
    segundos= segundos % (24 * 60 * 60)
    horas= segundos // (60 * 60)
    segundos = segundos % (60 * 60)
    minutos = segundos // 60
    segundos = segundos % 60
    print("{} Día/s | {} Hora/s | {} Minuto/s | {} Segundo/s".format(dias, horas, minutos, segundos))

if __name__ == "__main__":
    main()