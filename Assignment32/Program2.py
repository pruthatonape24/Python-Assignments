import schedule
import os
import datetime
import time

def MonitorFile(FileName):
    timestamp = datetime.datetime.now()

    Ret = False

    Ret = os.path.exists(FileName) 
    
    if(Ret==False):
        print("There is no such File with name", FileName)
        return

    Size = os.path.getsize(FileName)

    fobj = open("FileSizeLog.txt", "a")
    fobj.write("File Path : " + os.path.abspath(FileName) + "\n")
    fobj.write("File Size : " + str(Size) + " Bytes\n")
    fobj.write("Date : " + str(timestamp.date()) + "\n")
    fobj.write("Time : " + str(timestamp.time()) + "\n")
    fobj.close()

def main():
    FileName = input("Enter file name : ")

    schedule.every(30).seconds.do(MonitorFile, FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()