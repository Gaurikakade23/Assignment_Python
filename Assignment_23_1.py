class BookStore:
    NoofBooks =0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoofBooks +=1

    def Display(self):
        print(f"{self.Name}by {self.Author}.No of Books: {BookStore.NoofBooks}")   

obj1= BookStore("Linux System Programming","Robert Love")
obj1.Display()         
obj2= BookStore("C Programming","Dennis Rithie")
obj2.Display()   