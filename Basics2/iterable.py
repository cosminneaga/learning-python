# iterable
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# iterate
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
