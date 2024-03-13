# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# There is pseudocode availabe for you to guide you


# class Book
    # method initializer method with required state
    # parameters author and title
        # set self.author = author
        # set self.title = title

    # method get_author(self)
        # returns "Author: " + self.author

    # method get_title(self)
        # returns "Title: " + self.title

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def get_author(self):
        return "Author: " + self.author

    def get_title(self):
        return "Title: " + self.title

book= Book("Natalie Zina Walschots", "Hench")
print(book.get_author())  # prints "Author: Natalie Zina Walschots"
print(book.get_title())



