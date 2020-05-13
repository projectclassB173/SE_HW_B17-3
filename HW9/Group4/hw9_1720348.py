import random

class Per(object):
    def __init__(self, name, hp, level):
        self.name = name
        self.max = hp
        self._hp = hp
        self.level = level
    def get_name(self):
        return self.name
    def get_hp(self):
        return self._hp
    def get_level(self):
        return self.level
    def attack(self, target):
        raise NotImplementedError
    def __str__(self):
        return 'name:{}\t hp: {} \t level:{}'.format(self.name, self._hp, self.level)

class Hero(Per):
    def __init__(self, name, hp=40, level=1, race='elf'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.5
        elif self.race == 'elf':
            self.agile = 0.7

    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('你受到了{}点伤害'.format(hurt))
        else:
            print('Miss ')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-'*10, '你升级到{}级'.format(self.level), '-'*10)

class Monster(Per):
    def __init__(self, name, hp=30, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('怪兽受到了{}点伤害'.format(self.name, hurt))

class Boss(Per):
    def __init__(self, name, hp):
        super().__init__(name, hp, 4)
        self.shield = 30

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
        print("Boss收到{}点伤害".format(hurt))

def main():
    hero = Hero("yzj", 100, 1, 'elf')
    monster1 = Monster("虾兵")
    boss = Boss("龙王", 100)
    monster_list = [monster1, boss]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        monster = n_m(monster_list)
        while monster.get_hp() > 0:
            print('*'*10, '第{}回合'.format(r), '*'*10)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break
            print(hero)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = n_m(monster_list)

    if hero.get_hp() > 0:
        print('win，{}'.format(hero.get_name()))
    else:
        print("lose")

def n_m(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

if __name__ == '__main__':
    main()