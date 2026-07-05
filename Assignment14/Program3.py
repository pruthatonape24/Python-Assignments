#Maxnum = lambda no1, no2 : no1 > no2 and no1 or no2 
Maxnum = lambda No1, No2 : No1 > No2 == No1 or No2 < No1 == No1

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    
    ret = Maxnum(num1,num2)
    if ret == True:
            print("Maximum number is:", num1)
    else:
         print("maximum number is:", num2)

if __name__ =="__main__":
    main()
                     