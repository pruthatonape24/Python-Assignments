import threading
import time

def displayNum():
    print("Numbers from 1 to 50:")
    for i in range(1,51):
        print(i, end=" ")

def reverseNum():
    print("\nNumbers from 50 to 1:")
    time.sleep(2)
    for i in range(50,0,-1):
        print(i, end=" ")

def main():

    t1 = threading.Thread(target=displayNum)
    t2 = threading.Thread(target=reverseNum)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()