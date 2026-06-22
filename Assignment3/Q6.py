from sys import getsizeof 

def display(a):
    print(type(a))
    print(id(a))
    print(getsizeof(a))

def main():
    n = int(input("Enter the number:"))
    display(n)

if __name__ == "__main__":
    main()
