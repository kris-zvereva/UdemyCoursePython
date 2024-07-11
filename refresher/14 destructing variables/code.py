a = (5, 11) # a tuple. brackets may not be necessary
b = [(5, 11)]  # list with a tuple inside

x, y = 5, 11  # x = 5, y = 11

f = 5, 11
c, d = f  # c = 5, d = 11
print(c, d)


student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))  # gives a list of tuples

for t in student_attendance.items():
    print(t)  # destructing in tuples
    # print(f"{student}: {attendance}")


people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# a bad example, less readable
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# -- Ignoring values with underscore --
# if you use underscore as variable, it is meant to be ignored

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic


head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5]


*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

# -- Packing and unpacking --

