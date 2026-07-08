def Frequency(data, num):
    Count = 0
    for i in data:
        if i == num:
            Count+=1
    return Count

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("List:", Data)

    num = int(input("Enter the number:"))

    Ret = Frequency(Data,num)
    print("Frequency of number in list is:", Ret)

if __name__ == "__main__":
    main()