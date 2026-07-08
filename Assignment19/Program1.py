Power = lambda No : No ** 2

def main():
    num = int(input("Enter a number:"))
    ret = Power(num)
    print("Power of two is:",ret)

if __name__ == "__main__":
    main()