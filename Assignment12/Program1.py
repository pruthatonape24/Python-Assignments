def Vowel(data):
    if (data == "a" or data == "e" or data =="i" or data == "o" or data == "u"):
        return True
    else:
        return False
    
def main():
    ch = input("Enter a character:")
    ret = Vowel(ch)
    if ret == True:
        print("It is vowel")
    else:
        print("It is constant")

if __name__ == "__main__":
    main()
        