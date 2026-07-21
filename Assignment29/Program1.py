import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print("File is present")
    else:
        print("File is not present")

def main():
    Fname = input("Enter File name: ")
    CheckFile(Fname)

if __name__ == "__main__":
    main()