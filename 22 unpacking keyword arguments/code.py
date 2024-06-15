def named1(**kwargs):  # args and kwargs are usual but not mandatory names
    print(kwargs)


named1(name="Bob", age=23)  # {'name': 'Bob', 'age': 23}


def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named(**details)  # unpacking a dict into 2 named arguments


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():  # .items() cuz a dictionary
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# used to accept an unlimited number of arguments
def both(*args, **kwargs):  # all positioned args go into args, named into kwargs
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""

# While the implementation is irrelevant at this stage,
# what it allows is for the caller of `post()` to pass arguments to `request()`.
# example above simplifies request func because it adds 'post'


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error

