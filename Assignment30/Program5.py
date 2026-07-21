import schedule
import time
import datetime

def Display():
    fobj = open("Marvellous.txt","a")
    
    fobj.write("Task executed at : "+str(datetime.datetime.now())+"\n")
    fobj.close()
    

def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()