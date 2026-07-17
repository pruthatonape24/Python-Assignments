import multiprocessing

def Prime(num):
    if num <=1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True

def PrimeCount(N):
    count = 0
    for i in range(2,N+1):
        if Prime(i):
            count = count + 1
    
    return count

def main():
    Data = []
    
    val = int(input("Enter size of list:"))

    for i in range(val):
        No = int(input("Enter numbers:"))
        Data.append(No)

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount,Data)

    pobj.close()
    pobj.join()

    print("Prime count between 1 and N:",Result)

if __name__ == "__main__":
    main()