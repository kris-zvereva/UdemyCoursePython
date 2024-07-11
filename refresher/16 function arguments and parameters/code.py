# def fu(a, b):
#    pass  # do nothing


def add(x, y):  # x and y are parameters
    result = x + y
    print(result)


add(5, 3)  # 5 and 3 are arguments - they are values for parameters


def say_hello():  # no parameters, so no arguments if func is called
    print("Hello")


say_hello("Bob")  # error


def say_hi(name):
    print(f"hello, {name}!")


say_hi("Kris")


# positional arguments - positions they're in affects the values of its relevant parameter
def hi(name, surname):
    print(f"hi there, {name} {surname}")


hi("Kris", "Test")


# keyword arguments - not positional

def hi(name, surname):
    print(f"hi there, {name} {surname}")


hi(surname="Kris", name="Test")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)  # that's also ok, positional args go first
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments

