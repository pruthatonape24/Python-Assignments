import multiprocessing
import os

def Factorial(No):
    print(f"PID of Factorial : {os.getpid()} ")
    fact = 1
    
    for i in range(1, No+1):
        fact = fact * i

    return fact

def main():
    print(f"PID of Main : {os.getpid()} ")
    Arr = []
    
    Val = int(input("Enter size of list:"))

    for i in range(Val):
        No = int(input("Enter numbers:"))
        Arr.append(No)

    pobj = multiprocessing.Pool()

    Arr = pobj.map(Factorial,Arr)

    print("Data = ", Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()