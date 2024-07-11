print(5 == 5)
print(5 > 5)
print(10 != 10)

# all comparisons: ==, !=, >, <, >=, <=

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False. checked if they are they the same. the space is compared, not the lists themselves

friends = ["Rolf", "Bob"]
abroad = friends
print(friends is abroad)  # True

