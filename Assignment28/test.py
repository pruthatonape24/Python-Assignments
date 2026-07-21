#Program1 
def Display(FileName):
    try:
        fobj = open(FileName,"r")
        print("File gets opened")

        count = 0

        for line in fobj:
            count = count +1

        fobj.close()
        
        return count
    
    except FileNotFoundError as fobj:
        print("File is not present")

def main():
    Fname = input("Enter File name:")

    ret = Display(Fname)
    print("Count of Lines present in the file is:", ret)

if __name__ == "__main__":
    main()


#program 3
def Display(FileName):
    try:
        fobj = open(FileName, "r")
        print("File gets opened\n")

        line = fobj.readline()      

        while line != "":           
            print(line, end="")
            line = fobj.readline()  

        fobj.close()

    except FileNotFoundError:
        print("File is not present")

def main():
    Fname = input("Enter File name: ")

    Display(Fname)

if __name__ == "__main__":
    main()