class PlayerCharacter:

    membership = True  # class object attribute

    def __init__(self, name, age):
        if(age > 18):
            self.name = name  # attribute
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('ZOHO', 44)
player2 = PlayerCharacter('Tom', 12)
player2.attack = 50


print(player1)
print(player2.membership)
print(player2.attack)
player2.shout()
