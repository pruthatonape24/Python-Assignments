Cube = lambda No : No * No * No

def main():
    num = int(input("Enter number:"))
    ret = Cube(num)
    print("Cube is:", ret)
     

if __name__ == "__main__":
    main()