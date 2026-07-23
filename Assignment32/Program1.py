import schedule
import datetime
import time

def CreateFile():
    timestamp = datetime.datetime.now()

    FileName = "File_" + str(timestamp) + ".txt"
    FileName = FileName.replace(" ", "_")
    FileName = FileName.replace(":", "_")
    FileName = FileName.replace("-", "_")

    fobj = open(FileName, "w")

    fobj.write("File Name : " + FileName + "\n")
    fobj.write("Creation Date : " + str(timestamp.date()) + "\n")
    fobj.write("Creation Time : " + str(timestamp.time()) + "\n")

    fobj.close()

    print(FileName, "created successfully")

def main():
    schedule.every().minute.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()