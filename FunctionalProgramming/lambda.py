# lambda expressions
# one-time anonymus functions that you don't need more than once

# lambda param: action(param)

from functools import reduce
data = [1, 2, 3]


# map()
# def multp(item):
#     return item * 2


print()
print(list(map(lambda item: item * 2, data)))


# filter()
# def chk_odd(item):
#     return item % 2 != 0


print()
print(list(filter(lambda item: item % 2 != 0, data)))


# reduce()
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


print()
print(reduce(lambda acc, item: acc + item, data, 0))


print()
print(data)
