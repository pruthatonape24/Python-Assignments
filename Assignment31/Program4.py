import schedule
import time
import datetime

def NewLog():

    timestamp = datetime.datetime.now()

    LogFileName = "MarvellousLog_"+str(timestamp)+".txt"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")
    fobj.write("Log file created successfully \n")
    fobj.write("Creation Time: "+str(timestamp))
    
    fobj.close()

def main():
    schedule.every(10).minutes.do(NewLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()