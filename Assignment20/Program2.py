import threading

def EvenFactor(No):
    sum = 0
    for i in range(1, No+1):
        if No % i == 0 and i % 2 == 0:
            print("Even Factors:", i)
            sum +=i
    print("Sum of Even Factors is:", sum)

def OddFactor(No):
    sum = 0
    for i in range(1, No+1):
        if No % i == 0 and i % 2 != 0:
            print("Odd Factors:", i)
            sum +=i
    print("Sum of Odd number is:", sum)

def main():
    num = int(input("Enter Number:"))

    t1 = threading.Thread(target=EvenFactor, args=(num,))
    t2 = threading.Thread(target=OddFactor, args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()