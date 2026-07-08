def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    Num1 = int(input("Enter FIRST Number:"))
    Num2 = int(input("Enter SECOND Number:"))

    Ret = Add(Num1, Num2)
    print("Addition is:", Ret)

if __name__ == "__main__":
    main()