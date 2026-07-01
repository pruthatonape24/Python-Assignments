def PerfectNum(num):
    sum = 0 
    for i in range(1,num+1):
        if num % i == 0:
            sum += num 
        if sum == num:
            return True
        else:
            return False
            
def main():
    num = int(input("Enter number:"))
    ret = PerfectNum(num)
    if ret == True:
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")

if __name__ == "__main__":
    main()
    

