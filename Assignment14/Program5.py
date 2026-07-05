evennum = lambda No : No % 2 == 0 

def main():
    num = int(input("Enter number:"))
    
    ret = evennum(num)
    if ret == True:
            print("True")
    else:
         print("False")

if __name__ =="__main__":
    main()