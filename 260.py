'''260)Create a Book class that has two attributes:
.title
.author
and two methods:
A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')'''


class book:


    def __init__(self,title,author):
        self.title=title.title()
        self.author=author.title()

    def get_title(self):
        print("Title  :    ",(self.title))

    def get_author(self):
        print("Author is :  ",self.author)



author1=book('ip','MUKUT')
author1.get_title()
author1.get_author()