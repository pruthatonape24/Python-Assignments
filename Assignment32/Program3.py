import schedule
import os
import time

def Display(FileName):
    try:
        Ret = False

        Ret = os.path.exists(FileName) 
    
        if(Ret==False):
            print("There is no such File with name", FileName)
            return

        if os.path.getsize(FileName) == 0:
            print("File is empty")
            return

        fobj = open(FileName, "r")
        print("File Contents:", fobj.read())

        fobj.close()
    
    except PermissionError:
        print("Permission denied")

    except OSError:
        print("File cannot be opened")

def main():
    FileName = input("Enter file name : ")

    schedule.every().minute.do(Display, FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()