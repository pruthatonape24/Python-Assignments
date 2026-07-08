import threading

def smaller(small):
    print("TID of Smaller thread is:", threading.get_ident())
    print("Running in Thread:",threading.current_thread().name)
    smallchar = []
    count = 0
    for i in range(len(small)):
        if small[i] >= 'a' and small[i] <='z':
            smallchar.append(small[i])
            count +=1
    print("small characters are:", *smallchar)
    print("count of lowercase character is:", count)

def Capital(small):
    print("TID of Capital thread is:", threading.get_ident())
    print("Running in Thread:",threading.current_thread().name)
    upperchar =[]
    count = 0
    for i in range(len(small)):
        if small[i] >= 'A' and small[i] <='Z':
            upperchar.append(small[i])
            count +=1
    print("Uppercase character are:",*upperchar)
    print("count of uppercase character is:", count)

def digit(small):
    print("TID of digit thread is:", threading.get_ident())
    print("Running in Thread:",threading.current_thread().name)
    number =[]
    count = 0
    for i in range(len(small)):
        if small[i] >= '0' and small[i] <='9':
            number.append(small[i])
            count +=1
    print("Digits are:",*number)
    print("count of digits is:", count)

def main():
    print("TID of Main thread is:", threading.get_ident())
    print("Running in Thread:",threading.current_thread().name)
    small = input("Enter a string to check small and upper char and digit:")

    t1 = threading.Thread(target=smaller, args=(small,))
    t2 = threading.Thread(target=Capital, args=(small,))
    t3 = threading.Thread(target=digit, args=(small,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()