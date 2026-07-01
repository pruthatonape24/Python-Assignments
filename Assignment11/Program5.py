def Palindrome(data):
    digit = 0
    Reverse = 0
    while(data !=0):
        digit = data % 10
        Reverse = Reverse * 10 + digit
        data = data // 10
    return Reverse

def main():
    num = int(input("Enter a number:"))
    Ret = Palindrome(num)

    if Ret == num:
        print("It is Palindrome",Ret)
    else:
        print("It is not Palindrome", Ret)

if __name__ == "__main__":
    main()