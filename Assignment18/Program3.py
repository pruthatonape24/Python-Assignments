def Maximum(data):
    Max = 0
    for i in data:
        if i > Max:
            Max = i
    return Max

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    Ret = Maximum(Data)
    print("Maximum of number in list is:", Ret)

if __name__ == "__main__":
    main()