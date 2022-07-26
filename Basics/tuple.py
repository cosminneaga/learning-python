t = (1, 2, 3, 4, 5, 5)

print(t[1])
print(5 in t)


new_tuple = t[1:4]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)
print(y)
print(z)
print(other)


print(t.count(5))
print(t.index(5))
print(len(t))
