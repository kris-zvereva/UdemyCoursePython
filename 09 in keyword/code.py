friends = ["Kris", "Lisa", "Jen"]  # list
print("Jen" in friends)

# checking for membership

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print("Cool i've seen it too!")
else:
    print("never seen this one. you recommend?")

# The `in` keyword works in most sequences like lists, tuples, and sets.