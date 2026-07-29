import schedule
import os
import time

def DeleteEmpty(path):

    if not os.path.exists(path):
        print("Directory is not found")
        return

    log_file = open("DeletedFiles.log", "a")

    for file in os.listdir(path):

        filepath = os.path.join(path, file)

        if os.path.isdir(filepath):
            DeleteEmpty(filepath)

        else:
            try:
                if os.path.getsize(filepath)==0:
                    os.remove(filepath)
                    print("Deleted:", filepath)
                    log_file.write(filepath +"\n")

            except PermissionError:
                print("Permission denied:", filepath)

    log_file.close()

def main():
    directory = input("Enter a directory name : ")

    schedule.every().hour.do(DeleteEmpty, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()