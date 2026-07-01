def Even(N):
    i = 2
    while i <=N:
        print(i)
        i = i + 2

def main():
    Num = int(input("Enter a number:"))
    Ret = Even(Num)
    print("Even numbers are:",Ret)

if __name__ == "__main__":
    main()
    
    
    