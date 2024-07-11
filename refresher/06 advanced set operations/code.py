# -- Difference between two sets --

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)  # Rolf
print(local_friends)

#  local_friends = abroad.difference(friends)  # empty set set()


# -- Union of 2 sets --

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)


# -- Intersection of 2 sets --

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)

