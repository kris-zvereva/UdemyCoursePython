def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0")  # exception ZeroDivisionError: divisor cannot be 0
    return dividend / divisor


grades = []

print('welcome to the average grade program.')
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:  # e contains print(f'The average grade is {average}')
    print('there are no grades yet in your list')
else:  # runs if no error happened
    print(f'The average grade is {average}')
finally:  # runs no matter what
    print('thank you')

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [90]},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
