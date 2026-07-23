import schedule
import time

def display(Message):
    print(Message)

def main():
    Message = input("Enter message: ")
    Interval = int(input("Enter interval in seconds: "))

    if Interval <= 0:
        return
    
    schedule.every(Interval).seconds.do(display,Message)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()