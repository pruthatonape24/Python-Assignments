import multiprocessing
import os
import time 

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} ")
    sum = 0
    
    for i in range(2, No, 2):
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

    Arr = pobj.map(SumEven,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    
    print("Sum of even numbers:", Arr)

    print(f"Time required :{end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()