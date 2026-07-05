oddnum = lambda No : No % 2 != 0 

def main():
    num = int(input("Enter number:"))
    
    ret = oddnum(num)
    if ret == True:
            print("True")
    else:
         print("False")

if __name__ =="__main__":
    main()