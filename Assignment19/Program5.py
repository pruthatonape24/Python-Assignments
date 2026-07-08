from functools import reduce

def Prime(No):
    if No == 2:
        return True 
    
    for i in range(2,No):
        if No % i == 0:
            return False
        else:
            return True 
                
def Multi(No):
    return No * 2

def Max(No1,No2):
    return No1 if No1 > No2 else No2 

def main():
    Data = []
    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    print("List:", Data)

    FData = list(filter(Prime,Data)) 
    print("Prime number list:",FData)

    MData = list(map(Multi, FData)) 
    print("Multiply by 2:",MData)

    RData = reduce(Max,MData)
    print("Maximum number is:",RData)

if __name__ == "__main__":
    main()