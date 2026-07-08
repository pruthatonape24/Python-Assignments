def ChkNum(Num):
    if Num > 0:
        print("Positive Number")
    elif Num < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    value = int(input("Enter Number:"))
    ChkNum(value)

if __name__ == "__main__":
    main()