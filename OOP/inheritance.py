class User():
    def sign_in(self):
        return 'logged in'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


wizard = Wizard('Merlin', 50)

print(wizard.sign_in())
print(wizard.attack())

print()
w = Wizard('Merlin', 60)
print(isinstance(w, Wizard))
