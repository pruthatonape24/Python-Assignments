divnum = lambda No : No % 5 == 0 

def main():
    num = int(input("Enter number:"))
    
    ret = divnum(num)
    if ret == True:
            print("True")
    else:
         print("False")

if __name__ =="__main__":
    main()