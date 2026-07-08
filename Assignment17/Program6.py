def Pattern(No):
    for i in range(No,0,-1):
      for j in range(i):
            print("*", end= " ")
      print()

def main():
   num = int(input("Enter number:"))
   Pattern(num)
   

if __name__ == "__main__":
   main()