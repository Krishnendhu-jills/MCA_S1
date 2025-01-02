class Publisher:
    def _init_(self, name):
        self.__name=name
        
    def display(self):
        print("Name of Publisher: ", self.__name)
    
class Book(Publisher):
    def _init_(self, pubname, title, author):
        super()._init_(pubname)
        self.__pubname = pubname
        self.__title= title
        self.__author = author
        
    def display(self):
        super().display();
        print("Book Title:",self.__title)
        print("Book Author:",self.__author)
class Python(Book):
    def _init_(self,pubname, title, author,price, pages):
        super()._init_(pubname, title, author)
        self.__price=price
        self.__page=pages
    def display(self):
        super().display()
        print("Price of the book: ", self.__price)
        print("Number of pages: ", self.__page)
        
res = Python("DC Books", "Invisible Man", "Ralph Ellison", 250, 350)
res.display()