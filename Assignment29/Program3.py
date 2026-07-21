import sys

def CopyFile(FileName):
    fobj1 = open(FileName, "r")
    print("Existing file gets opened")

    fobj2 = open("Demo.txt", "w")
    print("Demo.txt gets created")

    data = fobj1.read()
    fobj2.write(data)

    fobj1.close()
    fobj2.close()

    print("Contents copied successfully")

def main():
    if len(sys.argv) != 1:
        print("You have to enter like Program3.py file_name")
        return
    
    Fname = sys.argv[1]

    CopyFile(Fname)

if __name__ == "__main__":
    main()