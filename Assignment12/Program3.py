def Addition(No1, No2):
    return No1 + No2

def Subtraction(No1,No2):
    return No1 - No2

def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    return No1 / No2

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))

    Ret1 = Addition(num1,num2)
    print("Addition is:", Ret1)

    Ret2 = Subtraction(num1,num2)
    print("Subtraction is:", Ret2)

    Ret3 = Multiplication(num1,num2)
    print("Multiplication is:", Ret3)

    Ret4 = Division(num1, num2)
    print("Division is:", Ret4)
    
if __name__ == "__main__":
    main()
    
    
    