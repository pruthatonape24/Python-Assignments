from functools import reduce

def Greaterthan(No):
    return No >= 70 and No <=90
        
def Increment(No):
    return No+10

def Product(No1,No2):
    return No1 * No2

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Input data is:",Data)

    FData = list(filter(Greaterthan,Data)) 
    print("Data after filter:",FData)

    MData = list(map(Increment, FData)) 
    print("Data after Map:",MData)

    RData = reduce(Product,MData)
    print("Data after Reduce:",RData)

if __name__ == "__main__":
    main()