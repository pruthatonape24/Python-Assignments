import threading

def Maximum(data):
    Max = 0
    for i in data:
        if i > Max:
            Max = i
    print("Maximum number:",Max)

def Minimum(data):
    Min = data[0]
    for i in data:
        if i < Min:
            Min = i
    print("Minimum number:",Min)

def main():
    Data = []

    size = int(input("Enter size of list:"))

    for i in range(size):
        No = int(input("Enter numbers:"))
        Data.append(No)

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()