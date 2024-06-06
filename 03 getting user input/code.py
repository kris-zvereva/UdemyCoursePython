name = input("enter your name: ")
print(name)
# input always gives a string

size_input = input("how big is your house in square feet: ")
square_feet = int(size_input)  # str -> int
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is {square_meters:.2f} square meters")  # :.2f makes 2 digits after

