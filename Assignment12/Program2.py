def Factors(data):
    i = 1 
    while i <= data:
        if data % i == 0:
           print(i)
        i = i+1

def main():
    num = int(input("Enter a number:"))
    print("Factors of this num:")
    Factors(num)

if __name__ == "__main__":
    main()