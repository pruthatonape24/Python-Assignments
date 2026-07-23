import schedule
import os
import time
import datetime

def CountFiles(DirectoryName):

    Count = 0

    for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
        Count = Count + len(FileNames)
   
    timestamp = datetime.datetime.now()

    fobj = open("DirectoryCountLog.txt","a")
    fobj.write("Directory Path:"+DirectoryName+"\n")
    fobj.write("Number of Files:"+str(Count)+"\n")
    fobj.write("Date and time:"+str(timestamp)+"\n")
    
    fobj.close()

def main():
    DirectoryName = input("Enter directory path:")

    schedule.every(5).minutes.do(CountFiles,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


