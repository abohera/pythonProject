PULGADA=1.0 # Valor de una pulgada
PULGADA_CM=2.54 # Valor de una pulgada en cm

def main():
# El usuario introducira los cm por teclado
    cm=int(input("Introduce los centimetros: "))
# Se hara la operacion y mostrara el resultado en pulgadas
    total=cm*(PULGADA/PULGADA_CM)
    print("El total en pulgadas son: %.2f in" % total)
    
if __name__ == "__main__":
   main()