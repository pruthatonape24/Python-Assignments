import schedule
import time

def Task1():
    print("Lunch Time!")

def Task2():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Task1)

    schedule.every().day.at("18:00").do(Task2)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()