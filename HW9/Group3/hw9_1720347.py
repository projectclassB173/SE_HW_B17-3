import random


class Person(object):
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
        return 'name:{}\t hp:{}\t level:{}\t'.format(self.name, self._hp, self.level)


class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='human'):
        super(Hero, self).__init__(name, hp, level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.4
        elif self.race == 'elves':
            self.agile = 0.8

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
            print('你受到{}攻击'.format(hurt))
        else:
            print('你没受到攻击')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('你升到{}级'.format(self.level))


class Monster(Person):
    def __init__(self,name,hp=20,level=1):
        super().__init__(name,hp,level)

    def attack(self,hero):
        if self.level == 1:
            hurt = random.randint(0,10)
        elif self.level == 2:
            hurt = random.randint(0,20)
        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('小怪兽受到{}攻击'.format(hurt))


class Boss(Person):
    def __init__(self,name,hp):
        super().__init__(name,hp,3)
        self.shield = 30

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
            print('BOSS受到{}攻击'.format(hurt))
        else:
            print('BOSS盾牌保护')


def main():
    hero = Hero('奥特曼', 100, 1, 'human')
    monster1 = Monster('小怪兽1')
    monster2 = Monster('小怪兽2')
    boss = Boss('哥斯拉', 100)
    monster_list = [monster1, monster2, boss]
    round = 1
    i = 0
    while i <= len(monster_list) and hero.get_hp() > 0:
        while monster_list[i].get_hp() > 0:
            print('**********ROUND{}**********'.format(round))
            hero.attack(monster_list[i])
            if monster_list[i].get_hp() > 0:
                monster_list[i].attack(hero)
                if hero.get_hp() <= 0:
                    break
            print(hero)
            print(monster_list[i])
            round += 1
        if monster_list[i].get_hp() <= 0:
            monster_list.remove(monster_list[i])
            hero.upgrade()
        if hero.get_hp() > 0:
            print('{}赢了'.format(hero.get_name()))
        else:
            print('{}输了'.format(hero.get_name()))


main()