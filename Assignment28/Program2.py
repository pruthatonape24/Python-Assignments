def Count(FileName):
    try:
        WordCount = 0

        fobj = open(FileName,"r")
        print("File gets opened")

        for i in fobj:
            count = i.split()
            WordCount = WordCount + len(count)

        fobj.close()
        
        return WordCount
    
    except FileNotFoundError as fobj:
        print("File is not present")

def main():
    Fname = input("Enter File name:")

    ret = Count(Fname)
    print("Count of Words present in the file is:", ret)

if __name__ == "__main__":
    main()