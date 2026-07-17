import threading

def Addition(data):
    Sum = 0
    for i in data:
        Sum = Sum + i
    print("Addition is:",Sum)

def Product(data):
    pr = 1
    for i in data:
        pr = pr * i
    print("Product is:",pr)

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    t1 = threading.Thread(target=Addition, args=(Data,))
    t2 = threading.Thread(target=Product, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()