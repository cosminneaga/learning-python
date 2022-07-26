from functools import reduce
data = [1, 2, 3]
data2 = [10, 20, 30]


# map()
def multp(item):
    return item * 2


print()
print(list(map(multp, data)))


# filter()
def chk_odd(item):
    return item % 2 != 0


print()
print(list(filter(chk_odd, data)))


# zip()
print()
print(list(zip(data, data2)))


# reduce()
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print()
print(reduce(accumulator, data, 0))


print()
print(data)
