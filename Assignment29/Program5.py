def Frequency(FileName,string):
    count = 0
    
    fobj = open(FileName, "r")

    data = fobj.read()
    line = data.split()

    for i in line:
        if i == string:
            count = count + 1
        
    fobj.close()

    return count 

def main():
    Fname = input("Enter File name:")
    String = input("Enter string:")

    Ret = Frequency(Fname,String)
    print("Frequency of the string is : ", Ret)

if __name__ == "__main__":
    main()