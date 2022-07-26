# binding the data into functions that manipulate the data and we encapsulate this in a single unit
# package everything up into the blueprint
# attributes
# methods


class Player:

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    # methods
    def speak(self):
        print(f'My name is {self.name} and I am {self.age} y.o.')
