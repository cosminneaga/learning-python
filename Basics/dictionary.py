dictionary = {
    'a': [1, 2, 3],
    'b': 'the value of b',
    'x': list(range(10)),
    456: [4, 5, 6],
    True: True,
}

print(dictionary)
print(dictionary['b'])
print(dictionary['a'][1])
print(dictionary[456])
print(dictionary[True])


user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
# get method returns None
print(user.get('age'))
# get default value
print(user.get('age', 55))


user2 = dict(name='John Doe')
print(user2)

# find
print('basket' in user)
print('size' in user)

# keys
print('greet' in user.keys())

# values
print('greet' in user.values())

# items as a tuple
print(user.items())

# copy
user3 = user.copy()
print(user3)

# pop
print(user.pop('basket'))
print(user)

# update
user.update({
    'age': 55
})
print(user)

# clear
user.clear()
print(user)
