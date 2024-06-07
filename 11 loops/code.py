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