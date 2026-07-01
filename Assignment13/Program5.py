def DisplayGrade(data):
    if data >= 75:
        print("Destination")
    elif data >= 60:
        print("First class")
    elif data >= 50:
        print("Second class")
    else:
        print("fail") 

def main():
    marks = int(input("Enter marks:"))
    print("Display grade:")
    DisplayGrade(marks) 

if __name__ == "__main__":
    main()