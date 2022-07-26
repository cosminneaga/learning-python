# hiding info and giving access to whatever is necessary
# private variables

class Player:

    def __init__(self, name, age):
        self._name = name  # private attribute
        self._age = age

    # abstracted
    def speak(self):
        print(f'My name is {self._name} and I am {self._age} y.o.')


pl = Player('Cosmin', 31)
pl.speak()
