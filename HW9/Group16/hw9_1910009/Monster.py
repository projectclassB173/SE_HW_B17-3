import random
from Role import Role


class Monster(Role):
    def __init__(self, name, hp):
        super(Monster, self).__init__(name=name, hp=hp, level=1)

    def attack(self, hero):
        hurt = random.randint(0, 10)
        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('Monster受到{}点伤害'.format(hurt))


class Boss(Role):
    def __init__(self, name, hp):
        super(Boss, self).__init__(name=name, hp=hp, level=3)
        self.shield = 30

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if (self.shield <= 0):
            self._hp -= hurt
        print("Boss受到{}点伤害".format(hurt))
