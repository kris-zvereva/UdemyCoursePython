def add(x, y):
    return x + y


print(add(5, 7))

# rewritten as a lambda

add = lambda x, y: x + y
print(add(5, 7))

# Four parts
# lambda key word
# parameters
# :
# return value

# Lambdas are meant to be short functions, often used without giving them a name.
# For example, in conjunction with built-in function map
# map applies the function to all values in the sequence


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [
    double(x) for x in sequence
]
doubled = map(double, sequence)  # goes over each value in sequence and applies double
print(list(doubled))

# -- Written as a lambda --

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))


# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.

