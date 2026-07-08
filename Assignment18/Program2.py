def Addition(data):
    Sum = 0
    for i in data:
        Sum = Sum + i
    return Sum

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    Ret = Addition(Data)
    print("Addition of numbers in list is:", Ret)

if __name__ == "__main__":
    main()