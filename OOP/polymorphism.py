# many forms
# the way in which object classes can shared same method name

class User():
    def sign_in(self):
        return 'logged in'

    # polymorphism
    def attack(self):
        return 'do nothing'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(User.attack(self))  # polymorphism
        return f'attacking with power of {self.power}'


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        return f'attacking with arrows: {self.arrows}'


w = Wizard('Merlin', 50)
a = Archer('Robin', 400)


print(w.attack())
print(a.attack())

print()


def player_attack(char):
    return char.attack()


print(player_attack(w))
print(player_attack(a))

print()
for char in [w, a]:
    print(char.attack())
