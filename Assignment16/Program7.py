def Divisible(Num):
    if Num % 5 == 0:
        return True
    else:
        return False
    
def main():
    value = int(input("Enter Number:"))
    Ret = Divisible(value)
    print(Ret)

if __name__ == "__main__":
    main()

    