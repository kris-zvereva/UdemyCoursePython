def add1(x, y):
    print(x + y)


add1(5, 8)   # 13
result = add1(5, 8)  #13
print(result)  # None - no value, undeclared value, missing value

# If we want to get something back from the function, it must return a value.
# All functions return _something_. By default, it's None.


def add(x, y):
    return x + y  # no brackets!


add(1, 2)  # Nothing printed out anymore.
result = add(2, 3)
print(result)  # 5


# -- Returning terminates the function --


def add(x, y):
    # return  # termination and returning nothing
    print(x + y)  # unreachable
    return x + y


result = add(5, 8)  # Nothing printed out
print(result)  # None, as is the first return

# -- Returning with conditionals --


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3)
print(result)  # 5

another = divide(15, 0)
print(another)  # You fool!


# exercise
# Complete the function by making sure it returns 42. .
def return_42():
    return 42
    # Complete function here
    # 'pass' just means "do nothing". Make sure to delete this!


# Create a function below, called my_function,
# that takes two arguments and returns the result of its two arguments multiplied together.
def my_function(x, y):
    return x*y

