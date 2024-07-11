movies_watched = {"The Matrix", "Green Book", "Her"}  # set of strings
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"Cool i've seen {user_movie} too!")
else:
    print("never seen this one. you recommend?")


number = 7
user_input = input("enter 'y' if you wanna play: ").lower()

if user_input == "y":  # OR user_input in ('y', 'Y')
    user_number = int(input("guess my number: "))
    if user_number == number:
        print("wow you've guessed")
    elif number - user_number in (1, -1):  # OR abs(number - user_number) == 1
        print("you were off by one")
    else:
        print("sorry it's wrong")

else:
    print("meh, ok then")

