l = [5, 4, 3]

# square each item
print(list(map(lambda item: item ** 2, l)))


# sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
