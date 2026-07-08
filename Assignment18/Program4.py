def Minimum(data):
    Min = data[0]
    for i in data:
        if i < Min:
            Min = i
    return Min

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    Ret = Minimum(Data)
    print("Minimum of number in list is:", Ret)

if __name__ == "__main__":
    main()