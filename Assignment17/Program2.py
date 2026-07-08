def Pattern(n):
    for i in range(n):
     print("*" * n)

def main():
   num = int(input("Enter number:"))
   Pattern(num)

if __name__ == "__main__":
   main()