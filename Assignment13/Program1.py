def rectangle(l,w):
    Area = l * w
    return Area

def main():
    length = int(input("Enter length:"))
    width = int(input("Enter width:"))
    ret = rectangle(length,width)
    print("Area of rectangle is:",ret)

if __name__ == "__main__":
    main()