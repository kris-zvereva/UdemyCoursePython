def hello():  # callable variable
    print("Hello")


hello()  # calling a function


def user_age_in_seconds():
    user_age = int(input("enter your age: "))
    age_seconds = user_age * 365 * 24 * 60
    print(f"your age in seconds is {age_seconds}.")


print("welcome to the age in seconds program!")
user_age_in_seconds()
print("goodbye!")


# -- Don't reuse names --


def print():
    print("Hello, world!")  # Error!


# -- Don't reuse names, it's generally confusing! --
friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]  # Another way of adding to a list!
    # f = friends + [friend_name] is ok


add_friend()
print(friends)  # Always ['Rolf', 'Bob']

# -- Can't call a function before defining it --

say_hello()


def say_hello():
    print("Hello!")


# -- Remember function body only runs when the function is called --


friends = []


def add_friend():
    friends.append("Rolf")


add_friend()

print(friends)  # [Rolf]
