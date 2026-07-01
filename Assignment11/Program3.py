def Sumof(data):
    digit = 0
    Sum = 0
    while(data !=0):
        digit = data % 10
        Sum = Sum + digit
        data = data // 10
    return Sum

def main():
    num = int(input("Enter a number:"))
    ret = Sumof(num)
    print("Sum of number",ret)

if __name__ == "__main__":
    main()