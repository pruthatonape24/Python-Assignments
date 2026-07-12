import multiprocessing
import os
import time 

def PowerCal(No):
    print(f"PID of Powercal : {os.getpid()} ")
    sum = 0
    
    for i in range(1, No+1):
        sum = sum + i ** 5

    return sum

def main():
    print(f"PID of Main : {os.getpid()} ")
    Data = []
    
    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(PowerCal,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    
    print("Result is:")
    print(Result)

    print(f"Time required :{end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()