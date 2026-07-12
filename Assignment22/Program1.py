import multiprocessing
def SumSqauare(No):
    Sum = 0
    
    for i in range(1, No+1):
        Sum = Sum + (i * i)

    return Sum

def main():
    Data = []
    
    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSqauare,Data)

    pobj.close()
    pobj.join()
    
    print("Result is:")
    print(Result)

if __name__ == "__main__":
    main()