import threading

def Even(No):
    result = []
    for i in range(1, No+1):
        if i % 2 == 0:
            result.append(i)
    print("First 10 Even number is:", *result)

def Odd(No):
    result = []
    for i in range(1, No+1):
        if i % 2 != 0:
            result.append(i)
    print("First 10 Odd number is:", *result)

def main():
    num = int(input("Enter Number:"))

    t1 = threading.Thread(target=Even, args=(num,))
    t2 = threading.Thread(target=Odd, args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()