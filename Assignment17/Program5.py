def PrimeNum(No):
    if No <=1:
        return False
    i = 2
    if No == i:
        return True
    
    if No % i == 0:
        return False
    else:
        return True
    
def main():
    Num = int(input("Enter a number:"))
    ret = PrimeNum(Num)

    if ret == True:
        print("It is a prime number" )
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()