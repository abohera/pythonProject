N=7

def main():
    for i in range(1, 8):
        i += 1
        for j in range(1, N-1):
            j += 1
            print(" ")
        for k in range(i, 1):
            k -= 1
            print(k)
        for x in range(2, i-1):
            x += 1
            print(x)

if __name__ == "__main__":
    main()