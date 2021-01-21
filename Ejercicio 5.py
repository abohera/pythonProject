def main():
    numero=0
    for numero in range(0,11):
        print(("\nTabla del %d") % (numero))
        for i in range(0,11):
            total=i*numero
            print(("%d*%d= %d")%(numero,i,total))

if __name__ == "__main__":
    main()