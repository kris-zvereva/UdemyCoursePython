friend_ages = {"Kris": 27,"Uta": 4, "Anne": 29}  # keys are int and str
friend_ages["Bob"] = 20

print(friend_ages["Bob"])  # subscript notation, indexes won't work, need a key

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends)
print(friends[0]["name"])  # Rolf Smith

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Rolf: 96
# Bob: 80
# Anne: 100

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

