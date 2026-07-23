import schedule
import time
import os
import datetime

def CheckDirectory():
    timestamp = datetime.datetime.now()
    totalfile = 0
    totalsubfolder = 0
    for Foldername, SubFolder, FileName in os.walk("Data"):
        totalfile = totalfile +len(FileName)
        totalsubfolder = totalsubfolder +len(SubFolder)

    print("Folder name is:",os.path.abspath("Data"))
    print("Total files are:", totalfile)
    print("Total subfolders are:", totalsubfolder)
    print("scan time is:", timestamp)

def main():
    schedule.every(1).minute.do(CheckDirectory)

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()