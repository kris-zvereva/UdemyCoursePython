number = 7

while True:  # infinite loop
    user_input = input("would you like to play? (Y/n): ")

    if user_input == "n":
        break  # exiting the loop

    user_number = int(input("guess my number: "))
    if user_number == number:
        print("wow you've guessed")
    elif abs(number - user_number) == 1:
        print("you were off by one")
    else:
        print("sorry it's wrong")


friends = ["Roman", "Lisa", "Max", "Anne"]

for friend in friends:
    print(f"{friend} is my friend")


for friend in range(4):
    print(f"{friend} is my friend")

# 0 is my friend
# 1 is my friend
# 2 is my friend
# 3 is my friend


# -- For loop 2 -- Average

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# another way. sum()
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)

# test
# Modify the code so that the evens list contains
# only the even numbers of the numbers list.
# You do not need to print anything.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)


# For part 2, add a clause to the if statement such that
# if the user's input is "q", your program prints "Quit".
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":  # elif is faster than just if here and less logical
    print("Quit")