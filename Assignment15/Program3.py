OddNum = lambda No : No % 2 != 0

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    FData = list(filter(OddNum, Data))
    print("list of odd numbers:", FData)

if __name__ == "__main__":
    main()