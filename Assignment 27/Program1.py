class BookStore:
    NoofBooks = 0 

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoofBooks = BookStore.NoofBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books:{BookStore.NoofBooks}")

def main():
    BookName = input("Enter a Bookname:")
    Author = input("Enter a Author name:")

    obj1 = BookStore(BookName,Author)
    obj1.Display()

    BookName = input("Enter a Bookname:")
    Author = input("Enter a Author name:")

    obj2 = BookStore(BookName,Author)
    obj2.Display()

if __name__ == "__main__":
    main()