def CopyFile(ExistingFile, NewFile):
    try:
        fobj1 = open(ExistingFile, "r")
        fobj2 = open(NewFile, "w")

        data = fobj1.read()
        fobj2.write(data)

        fobj1.close()
        fobj2.close()

        print("Contents copied successfully")

    except FileNotFoundError :
        print("File is not present")

def main():
    Fname1 = input("Enter existing file name: ")
    Fname2 = input("Enter new file name: ")

    CopyFile(Fname1, Fname2)

if __name__ == "__main__":
    main()