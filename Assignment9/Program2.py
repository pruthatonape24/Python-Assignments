def ChkGreater(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2
    
def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    Ret = ChkGreater(Value1, Value2)
    print("Greater number is:", Ret)

if __name__ == "__main__":
    main()