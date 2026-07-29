import schedule
import os
import time
import shutil

def Display(name, dist):
    if not os.path.exists(name):
        print("Source directory is not present")
        return

    if not os.path.exists(dist):
        os.mkdir(dist)
        print(f"Destination directory {dist} created")

    log_file = "Marvellous.log"

    for files in os.listdir(name):
        if files.endswith(".txt"):
            src_file = os.path.join(name, files)
            des_file = os.path.join(dist, files)

            try:
                shutil.copy2(src_file, des_file)
                print(f"Copied {src_file} -> {des_file}")

            except PermissionError:
                print(f"Skipped {src_file} (file in use)")
            except Exception as e:
                print(f"Error copying {src_file}:{e}")

def main():
    name = input("Enter a source directory name : ")
    dest = input("Enter a destination directory name : ")

    schedule.every(10).minutes.do(Display, name, dest)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()