print(enumerate('Hello'))

print()
for char in enumerate('Hello'):
    print(char)

print()
for char in enumerate([1, 2, 3]):
    print(char)

print()
for i, no in enumerate(list(range(1, 101))):
    if no == 50:
        print(f'Index of no 50 is: {i}')
