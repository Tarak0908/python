class Book:
    def __init__(self,title):
        self.title=title
def create_book_list():
        return[Book("python 101"),Book("AI basics"),Book("data science")]
books=create_book_list()
for b in books:
    print("Book title:",b.title)




Book title: python 101
Book title: AI basics
Book title: data science
