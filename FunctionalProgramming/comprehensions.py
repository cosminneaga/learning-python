# list, set and dictionary comprehensions

# [param for param in iterable]

l = [char for char in 'hello']
l2 = [no for no in range(0, 100)]
l3 = [no ** 2 for no in range(0, 100)]
l4 = [no ** 2 for no in range(0, 100) if no % 2 == 0]
# for c in 'hello':
#     l.append(c)

print(l)
print()
print(l2)
print()
print(l3)
print()
print(l4)


# set
s = {char for char in 'hello'}
print()
print(s)

# dictionary
sd = {
    'a': 2,
    'b': 3,
    'c': 4
}
d = {key: value ** 2 for key, value in sd.items()}
d1 = {key: value ** 2 for key, value in sd.items() if value & 2 == 0}
print()
print(sd)
print(d)
print(d1)


d2 = {value: value * 2 for value in [1, 2, 3]}
print(d2)
