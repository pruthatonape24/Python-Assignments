import threading

def Prime(data):
    print("Prime numbers are:.",end=" ")
    for num in data:
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                    print(num,end=" ")
    print()
        
def NonPrime(data):
    print("Non-Prime numbers are:",end=" ")
    for num in data:
        if num <=1:
            print(num,end="")
        else:
            for i in range(2,num):
                if num % i == 0:
                    print(num,end=" ")
                    break
    print()

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
                