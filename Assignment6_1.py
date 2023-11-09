
class Bookstore:
    No_Of_Books = 0

    def __init__(self):
        self.Name = input("Enter name of book you want:")
        self.Author =input("Enter a Author of Book:")
        Bookstore.No_Of_Books +=1

    def Display(self):
        print("Name of Book:",self.Name)
        print("Author of Books:",self.Author)
        print("Number of Book :",Bookstore.No_Of_Books)

def main():

    obj1 = Bookstore()
    obj1.Display()
        
    print()
    
    obj2 = Bookstore()
    obj2.Display()
    

if __name__ == "__main__":
    main()