class Toy:
    def __init__(self, color, age) -> None:
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'YOYO',
            'has_pets': False
        }

    # modifying a built-in dunder method
    def __str__(self) -> str:
        return f'{self.color}'

    # modifying a built-in dunder method
    def __len__(self):
        return 5

    # modifying a built-in dunder method
    def __del__(self):
        print('deleted!')

    # modifying a built-in dunder method
    def __call__(self):
        return 'yesss??'

    # modifying a built-in dunder method
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)

print()
print(dir(action_figure))

print()
print(action_figure.__str__())
print(str(action_figure))

print()
print(len(action_figure))


print()
print(action_figure())

print()
print(action_figure['name'], action_figure['has_pets'])

print()
del action_figure
