def CountN(data):
    digit = 0
    count = 0
    while (data !=0):
        digit = data % 10
        data = data // 10
        count = count+1
    return count

def main():
    num =int(input("enter number:"))
    ret = CountN(num)
    print("the number of digits is:", ret)

if __name__ == "__main__":
    main()


