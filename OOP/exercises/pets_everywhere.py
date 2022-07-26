class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


class Cindy(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
simon = Simon('Simon', 2)
sally = Sally('Sally', 1.5)
cindy = Cindy('Cindy', 5)

for cat in [simon, sally, cindy]:
    print(cat.name, cat.age)
    sound = cat.sing('meowwww')
    print(f'{cat.name} sounds like: {sound}')
