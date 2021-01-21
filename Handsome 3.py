DIV=100
PENALTY=2

def main():
    discount=int(input("Introduce el porcentaje del descuento: "))
    product=float(input("Introduce el precio del producto: "))
    if product >= 100:
        price=(product*discount)/DIV
        print(product-price)
    elif product < 30:
        price=(product*PENALTY)/DIV
        print(product+price)
    elif product < 99 and product > 30:
        print(int(product))
        
if __name__ == "__main__":
    main()