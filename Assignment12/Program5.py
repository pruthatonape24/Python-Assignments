def Reversenum(data):
    while data >= 1:
        print(data)
        data = data -1

def main():
    num = int(input("Enter a number:"))
    print("Numbers in reverse order is:")
    Reversenum(num)

if __name__ == "__main__":
    main()