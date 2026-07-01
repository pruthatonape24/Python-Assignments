def Square(No):
    Ans = No * No
    return Ans

def main():
    Value = int(input("Enter number:"))

    Ret = Square(Value)
    print("Square of number is:", Ret)

if __name__ == "__main__":
    main()
    