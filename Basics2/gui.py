picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    string = ''
    for column in row:
        if column == 0:
            string += ' '
        else:
            string += '*'
    print(string)

print()
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
