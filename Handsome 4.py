def main():
    numberone=int(input("Introduce el primer número: "))
    numbertwo=int(input("Introduce el segundo número: "))
    numberthree=int(input("Introduce el tercer número: "))
    if numberone < 0:
        print(numberone*numbertwo*numberthree)
    else:
        print(numberone+numbertwo+numberthree)

if __name__ == "__main__":
    main()