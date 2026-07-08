import MarvellousNum
    
def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("List:", Data)

    Ret = MarvellousNum.AddPrime(Data)
    print("Addition of Prime number in list is:", Ret)

if __name__ == "__main__":
    main()