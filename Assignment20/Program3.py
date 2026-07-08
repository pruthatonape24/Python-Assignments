import threading

def Even(data):
    sum = 0
    result = []
    for No in data:
        if No % 2 == 0:
            result.append(No)
            sum = sum + No
    print("Even numbers:",*result)
    print("Sum of Even number is:", sum)

def Odd(data):
    sum = 0
    result =[]
    for No in data:
        if No % 2 != 0:
            result.append(No)
            sum = sum + No
    print("Odd numbers:",*result)
    print("Sum of Odd number is:", sum)

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        num = int(input("Enter numbers:"))
        Data.append(num)

    t1 = threading.Thread(target=Even, args=(Data,))
    t2 = threading.Thread(target=Odd, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()