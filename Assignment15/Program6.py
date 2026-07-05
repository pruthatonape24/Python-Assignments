from functools import reduce

MinElement = lambda No1, No2 : No1 < No2 and No1 or No2

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    RData = reduce(MinElement, Data)
    print("Minimum element is:", RData)

if __name__ == "__main__":
    main()