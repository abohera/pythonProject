BYTE=1024 # Valor de un byte

def main():
# El usuario introducira los megabytes por teclado
    mb=int(input("Introduce los megabytes: "))
# Se hara la operacion y mostrara el resultado en bytes
    total=(mb*BYTE)*BYTE
    print("El total en bytes son: %u bytes" % total)
    
if __name__ == "__main__":
   main()
