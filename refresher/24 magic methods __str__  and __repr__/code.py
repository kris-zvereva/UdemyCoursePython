class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Person("Bob", 35)
print(bob)  # <__main__.Person object at 0x105039990>


# -- __str__ --
# The goal of __str__ is to return a nice, easy to read string for end users.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob)  # Person Bob, 35 years old

# -- __repr__ --
# The goal of __repr__ is to be unambiguous, and if possible what it outputs should allow us to re-create an identical object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # unambiguous representation of an object which can be used to recreate the object
        # I'm adding the < > just so it's clear that this is an object we're printing out!
        return (
            f"<Person({self.name!r}, {self.age})>"
        )  # !r calls the __repr__ method of the thing.


bob = Person("Bob", 35)
print(bob)  # <Person('Bob', 35)>


# exercise

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        total = 0
        for item in self.items:
            total = total + item['price']
            return total
        # OR
        # return sum([item['price'] for item in self.items])
        # Add together all item prices in self.items and return the total.

