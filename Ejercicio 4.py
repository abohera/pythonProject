N=7

def main():
    for i in range(N):
        k = i + 1
        for j in range(N-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(k, end="")
            k = k - 1
        if i>0:
            for j in range(i-1):
                print(" ", end="")
            for j in range(i+1):
                k = k + 1
                print(k, end="")

if __name__ == "__main__":
    main()