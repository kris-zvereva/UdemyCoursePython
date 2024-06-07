numbers = [1, 3, 5]
doubles = [x * 2 for x in numbers]


friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# same as
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)


print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "start_s: ", id(starts_s))  # diff places in memory

