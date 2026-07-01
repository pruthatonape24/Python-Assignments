def Factorial(data):
    fact = 1
    for i in range(1, data +1):
        fact = fact * i
    return fact

def main():
    Value = int(input("Enter a number:"))
    Ret = Factorial(Value)
    print("Factorial of is:", Ret)

if __name__ == "__main__":
    main()