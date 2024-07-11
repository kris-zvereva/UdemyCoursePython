# -- String formatting

name = "Bob"
greeting = f"Hello, {name}"

print(f"Hello, {name}")

name = "Rolf"
print(f"Hello, {name}")

name = "Kris"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name2 = greeting.format("Rob")

print(with_name)
print(with_name2)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Jane", "Thursday")
print(formatted)



