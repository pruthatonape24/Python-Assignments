def CheckWord(FileName, Word):
    try:
        fobj = open(FileName, "r")
        print("File gets opened")

        data = fobj.read()

        if Word in data:
            print("Word is present in the file")
        else:
            print("Word is not present in the file")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present")

def main():
    Fname = input("Enter File name: ")
    Wname = input("Enter Word to search: ")

    CheckWord(Fname, Wname)

if __name__ == "__main__":
    main()