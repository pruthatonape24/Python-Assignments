import multiprocessing
import os
import time 

def Even(No):
    print(f"PID of Even : {os.getpid()} ")
    count = 0
    
    for i in range(2, No, 2):
        count = count + 1

    return count

def main():
    print(f"PID of Main : {os.getpid()} ")
    Arr = []
    
    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Arr.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Arr = pobj.map(Even,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    
    print("Count of even numbers:", Arr)

    print(f"Time required :{end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()