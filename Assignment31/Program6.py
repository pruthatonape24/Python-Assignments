import schedule
import time

def Mon():
    print("Start Your weekly goals")

def Wed():
    print("Review your weekly progress")

def Fri():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(Mon)
    schedule.every().wednesday.at("17:00").do(Wed)
    schedule.every().friday.at("18:00").do(Fri)

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()