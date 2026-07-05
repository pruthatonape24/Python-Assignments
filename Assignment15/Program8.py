Divby = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Enter the number:", Data)

    FData = list(filter(Divby, Data))
    print("list of numbers divisible by 3 and 5:", FData)

if __name__ == "__main__":
    main()