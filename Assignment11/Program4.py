def ReverseNum(data):
    digit = 0
    Reverse = 0
    while(data !=0):
        digit = data % 10
        Reverse = Reverse * 10 + digit
        data = data // 10
    return Reverse

def main():
    num = int(input("Enter a number:"))
    ret = ReverseNum(num)
    print("Reverse number",ret)

if __name__ == "__main__":
    main()