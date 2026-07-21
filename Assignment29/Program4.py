import sys

def CompareFile(FileName1, FileName2):
    fobj1 = open(FileName1, "r")
    fobj2 = open(FileName2, "r")

    if (fobj1.readlines() == fobj2.readlines()) :
        print("Success")
    else:
        print("Failure")

    fobj1.close()
    fobj2.close()

def main():
    if len(sys.argv) != 3:
        print("You have to enter like Program4.py file_name1 file_name2")
        return
    
    Fname1 = sys.argv[1]
    Fname2 = sys.argv[2]

    CompareFile(Fname1, Fname2)

if __name__ == "__main__":
    main()