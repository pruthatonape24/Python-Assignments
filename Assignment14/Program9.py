Multiplication = lambda No1, No2 : No1 * No2

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    ret = Multiplication(num1, num2)
    print("Multiplication is:", ret)

if __name__ == "__main__":
    main()