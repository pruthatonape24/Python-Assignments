def Display(FileName):
    try:
        fobj = open(FileName, "r")
        print("File gets opened\n")

        for line in fobj:
            print(line, end="")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present")

def main():
    Fname = input("Enter File name: ")

    Display(Fname)

if __name__ == "__main__":
    main()