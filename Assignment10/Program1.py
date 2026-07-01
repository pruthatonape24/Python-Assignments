def MultTable(n):
    for i in range(1, 11, 1):
        result = n * i 
        print(result)
    
def main():
    Value = int(input("Enter a number:"))

    Ret = MultTable(Value)
    print("Multiplication Table of", Value, "is:", Ret)
    
if __name__ == "__main__":
    main()
