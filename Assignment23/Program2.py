import multiprocessing
import os
import time 

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} ")
    sum = 0
    
    for i in range(1, No, 2):
        sum = sum + i 

    return sum

def main():
    print(f"PID of Main : {os.getpid()} ")
    Arr = []
    
    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Arr.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Arr = pobj.map(SumOdd,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    
    print("Sum of odd numbers:", Arr)

    print(f"Time required :{end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()