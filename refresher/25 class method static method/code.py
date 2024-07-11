# all functions that use the object(=instance)
# as first parameter are called instance methods


class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):  # parameter always the same, it's class itself
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():  # doesn't get anything when called
        print("Called static method")


test = ClassTest()
# 8 and 9 lines do the same
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()
# Called class_method of <class '__main__.ClassTest'>

ClassTest.static_method()
# Called static method


# Instance methods are used for most things.
# When you want to produce an action that uses the data stored in an object.
# Static methods are used to just place a method inside a class
# because you feel it belongs there (i.e. for code organisation, mostly)
# Class methods are often used as factories. Not used much


# HOW TO USE CLASS METHODS
# using them for creating new objects inside the class
class Book:
    TYPES = ("hardcover", "paperback")  # variable inside a class is a class property

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight)


print(Book.TYPES)
# line below is not needed because of class methods
# book = Book('Harry Potter', 'hardcover', 1500)
# print(book.name)  # Harry Potter
# print(book)  # <Book Harry Potter, hardcover, weighing 1500g>

book = Book.hardcover("Harry Potter", 1500)
print(book)  # <Book Harry Potter, hardcover, weighing 1600g>
light = Book.paperback("Python 101", 600)
print(light)  # <Book Python 101, paperback, weighing 600g>


# exercise
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

