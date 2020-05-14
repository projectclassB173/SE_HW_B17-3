import random
from Role import Role


class Hero(Role):
    def __init__(self, name, hp, level, race):
        super(Hero, self).__init__(name=name, hp=hp, level=level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.4
        elif self.race == 'elves':
            self.agile = 0.8

    def attack(self, monster):
        hurt = random.randint(0, 10*self.level)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print("你受到{}点攻击".format(hurt))
        else:
            print("你躲避了攻击！")

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('你升级到了{}级'.format(self.level))
