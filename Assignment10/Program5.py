def Odd(N):
    i = 1
    while i <=N:
        print(i)
        i = i + 2
        
def main():
    Num = int(input("Enter a number:"))
    Ret = Odd(Num)
    print("Odd numbers are:",Ret)

if __name__ == "__main__":
    main()
    