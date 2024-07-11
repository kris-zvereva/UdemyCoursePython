def multiply(*args):  # used to collect the arguments
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


multiply(1, 3, 5)  # (1, 3, 5) a tuple of arguments
print(multiply(1, 3, 5))  # (1, 3, 5)  15
print(multiply(-1, 3))  # (-1, 3)  -3


def add(x, y):
    return x + y


nums = [3, 5]
add(*nums)  # destructuring the list for each parameter
print(add(*nums))  # 8
print(add(x=3, y=5))  # also works


nums = {"x": 15, "y": 25}
print(add(nums["x"], nums["y"]))  # 40
print(add(x=nums["x"], y=nums["y"]))  # 40

# OR
print(add(**nums))  # 40


def apply(*args, operator):  # named arg at the end
    if operator == "*":  # asterisk
        return multiply(*args)  # otherwise it'll be a tuple inside a tuple
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 5, "+"))  # error
print(apply(1, 3, 6, 7, operator="+"))  # 17
print(apply(1, 3, 6, 7, operator="*"))  # 126

