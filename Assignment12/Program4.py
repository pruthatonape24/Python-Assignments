def Startnum(data):
    digit = 1
    while digit <= data:
        print(digit)
        digit = digit +1
    

def main():
    num = int(input("Enter a number:"))
    print("numbers starting from 1 up to",num,"is:")
    Startnum(num)

if __name__ == "__main__":
    main()
