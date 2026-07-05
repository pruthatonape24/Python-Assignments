Square = lambda No : No * No

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    MData = list(map(Square, Data))
    print("list of Square numbers:", MData)

if __name__ == "__main__":
    main()