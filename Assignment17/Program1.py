from Arithmatic import *

def main():
    Value1 = int(input("Enter First Number:"))
    Value2 = int(input("Enter Second Number:"))

    Ret = Add(Value1, Value2)      
    print("Addition is:",Ret)

    Ret1 = Sub(Value1, Value2)  
    print("Subtraction is:", Ret1)

    Ret2 = Multi(Value1, Value2)
    print("Multiplication is:", Ret2)

    Ret3 = Div(Value1, Value2)
    print("Division is:", Ret3)

if __name__ == "__main__":
    main()