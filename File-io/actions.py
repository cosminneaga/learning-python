# read - mode='r'
print()
with open('File-io\sample.txt', mode='r') as file:
    print(file.readlines())


print()


# read&write - mode='r+'
with open('File-io\write.txt', mode="r+") as file:
    text = file.write('hello this is Cosmin')
    print(text)


# append - mode='a'
with open('File-io\write.txt', mode="a") as file:
    text = file.write(':)')
    print(text)


# write - mode='w'
# write also creates a new file or overrides a created one
with open("File-io\\folder\sad.txt", mode="w") as file:
    text = file.write(':(')
    print(text)


# relative path
# File-io\actions.py

# absolute path
# D:\Learning\Python\Udemy\Complete Python Developer in 2022 Zero to Mastery\File-io\actions.py


try:
    with open("File-io\\folder\sa.txt", mode="r") as file:
        text = file.read()
        print(text)
except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(e)
