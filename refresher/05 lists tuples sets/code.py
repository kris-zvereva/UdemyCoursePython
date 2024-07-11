l = ["Kris", "Anne", "Lisa"]  # list - can add and remove elements. keep order of elements
t = ("Kris", "Anne", "Lisa")  # tuple - can't modify elements. keep order of elements
s = {"Kris", "Anne", "Lisa"}  # set - can't have duplicates in it. doesn't keep order of elements, can't be modified after created

# Access individual items in lists and tuples using the index. subscript notation

print(l[0])
print(t[2])
# print(s[0])  # gives an error because sets are unordered

l[1] = "Kate"  # modify individual items in lists using the index

print(l)

# Add or remove items from the list
l.append("Anne")
print(l)

l.remove("Lisa")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)


s.add("Bob")
s.add("Bob")  # makes no sense, can't have duplicates
print(s)

# Create a tuple, called my_tuple, with a single value in it
my_tuple = ('c',)

