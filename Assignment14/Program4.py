Minnum = lambda No1, No2 : No1 < No2 and No1 or No2

def main():
    num1 = int(input("Enter First number:")) 
    num2 = int(input("Enter Second number:"))
    ret = Minnum(num1, num2)
    print("Minimum number is:", ret)

if __name__ == "__main__":
    main()