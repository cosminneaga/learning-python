s = {1, 2, 3, 4, 5, 5}

print(s)

# add
s.add(2)
s.add(100)
print(s)

print(100 in s)
print(len(s))


print(list(s))


copied = s.copy()
print(copied)


s.clear()
print(s)

print('SET METHODS')
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# s.difference()
print('s.difference()')
print(my_set.difference(your_set))
print(your_set.difference(my_set))

# s.intersection()
print('s.intersection()')
print(my_set.intersection(your_set))

# s.isdisjoint()
print('s.isdisjoint()')
print(my_set.isdisjoint(your_set))

# s.issubset()
print('s.issubset()')
print(my_set.issubset(your_set))

# s.issuperset()
print('s.issuperset()')
print(my_set.issuperset(your_set))

# s.union()
print('s.union()')
print(my_set.union(your_set))

# s.discard()
print('s.discard()')
my_set.discard(5)
print(my_set)

# s.difference_update()
print('s.difference_update()')
my_set.difference_update(your_set)
print(my_set)
print(your_set)
