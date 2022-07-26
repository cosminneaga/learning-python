class Player:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    @classmethod
    def adding(cls, n1, n2):
        print(cls)
        return n1 + n2

    @staticmethod
    def noAccessToCls(n1, n2):
        return n1 + n2


# player1 = Player()
print(Player.adding(2, 3))
print(Player.noAccessToCls(2, 3))
