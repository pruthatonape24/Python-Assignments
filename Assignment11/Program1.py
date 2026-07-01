def Prime(N):
    if N <=1:
        return False
    i = 2
    if N % i == 0:
        return False
    elif N == 2:
        return True 
    else:
        i = i + 1
        return True

def main():
    Num = int(input("Enter a number:"))
    ret = Prime(Num)

    if ret == True:
        print(ret ,"is a prime number" )
    else:
        print(ret , "is not a prime number")

if __name__ == "__main__":
    main()
    