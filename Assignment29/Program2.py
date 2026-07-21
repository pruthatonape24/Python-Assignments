import sys
import os

def Display(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName, "r")
        print(fobj.read())
        fobj.close()
    else:
        print("File is not present")

def main():
    Fname = sys.argv[1]
    Display(Fname)

if __name__ == "__main__":
    main()