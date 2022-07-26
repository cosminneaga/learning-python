class User():
    def sign_in(self):
        return 'logged in'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'attacking with power of {self.power}'


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def chk_arr(self):
        return f'{self.arrows} arrows remaining'

    def run(self):
        return 'ran really fast'


# MULTIPLE INHERITANCE
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('Borgie', 50, 100)
print(hb1.run())
print(hb1.chk_arr())
print(hb1.attack())
print(hb1.sign_in())
