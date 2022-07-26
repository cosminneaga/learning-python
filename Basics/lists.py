basket = [1, 2, 3, 4, 5]
print(basket)
print(f'Length {len(basket)}')

# append to end
basket.append(6)
print(basket)

# insert on index
basket.insert(2, 100)
print(basket)

# extends a list with a list
basket.extend([101, 102])
print(basket)

# pop returns the removed value
# pop from end
basket.pop()
print(basket)

# pop from index
basket.pop(0)
print(basket)

# remove by value
basket.remove(100)
print(basket)

# clear
basket.clear()
print(basket)


basket = [1, 2, 3, 4, 5]
print('coming back')
print(basket)
# index
# finds the index of a value
print(basket.index(2))

# define the start & stop index to minimize the search
print(basket.index(2, 0, 2))

# check if in
print(2 in basket)
print(100 in basket)
print('i' in 'Hi my name is Ian')

# count
print(basket.count(2))
print('Hi my name is Ian'.count('i'))

# sort
basket = [2, 4, 1, 5, 3]
basket.sort()
print(basket)


# sorted func produces a new array
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(sorted(basket))
print(basket)


# copy
new_basket = basket.copy()
print(new_basket)

# reverse
basket.sort()
basket.reverse()
print(basket)


print(basket[::-1])


# generate list
# from zero
basket = list(range(100))
print(basket)
# start at one
basket = list(range(1, 100))
print(basket)


# join lists
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(sentence)
print(new_sentence)


# unpacking
print('LISTS UNPACKING')
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print(b)
print(c)
print(other)
print(d)
