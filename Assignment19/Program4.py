from functools import reduce

def EvenNum(No):
    return No % 2 == 0
        
def Square(No):
    return No * No

def Addition(No1,No2):
    return No1 + No2

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("Input data is:",Data)

    FData = list(filter(EvenNum,Data)) 
    print("Data after filter:",FData)

    MData = list(map(Square, FData)) 
    print("Data after Map:",MData)

    RData = reduce(Addition,MData)
    print("Data after Reduce:",RData)

if __name__ == "__main__":
    main()