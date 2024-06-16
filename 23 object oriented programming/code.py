student = {"name": "Rolf",
           "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student['grades']))
# print(student.average()) will not work yet


class Student:  # definition of something without actually creating it yet
    def __init__(self):  # method - a func inside a class
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()  # creating a new object that behaves as this class defines
# by calling init method
print(student.name)  # Rolf
print(student.grades)

# calling average method inside Student class
# and self parameter take value of student variable which has an object that was created in line22
print(Student.average_grade(student))
# OR call it on the object
print(student.average_grade())


# -- Parameters in __init__ --

class Student:
    def __init__(self, name, grades):  # can have other parameters
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 90, 90, 90, 100, 100))
student2 = Student("Rolf", (75, 80, 90, 90, 100, 100))
print(student.average())
print(student2.average())

# -- Remember *args ? --

class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", 36, 67, 90, 100, 100)
print(student.average())


