# I/O - input/output

# input image
# output compressed image

file = open('File-io/sample.txt')

print()
print(file.read())
file.seek(0)
print(file.read())

print()
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

print()
file.seek(0)
print(file.readlines())


file.close()
