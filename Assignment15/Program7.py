StrLen = lambda String : len(String) > 5

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        data = input("Enter data:")
        Data.append(data)

    print("Enter the number:", Data)

    FData = list(filter(StrLen, Data))
    print("list of strings with length greater than 5:", FData)

if __name__ == "__main__":
    main()