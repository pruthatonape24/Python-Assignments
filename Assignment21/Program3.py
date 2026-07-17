import threading

counter = 0
lock = threading.Lock()

def Increment(n):
    global counter

    for i in range(n):
        lock.acquire()
        counter = counter+1
        lock.release()

def main():
    n = int(input("Enter number:"))

    t1 = threading.Thread(target=Increment,args=(n,))
    t2 = threading.Thread(target=Increment,args=(n,))
    t3 = threading.Thread(target=Increment,args=(n,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()