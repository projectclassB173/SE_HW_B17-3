from random import randint, randrange

class Hero(object):

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, monster):
        monster.hp -= randint(0, 25)

    def __str__(self):
        return '%s英雄\n' % self._name + \
               '生命值：%d\n' % self._hp

class Monster(object):

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def attack(self, hero):
        hero.hp -= randint(0, 15)

    def __str__(self):
        return '%s小怪兽\n' % self.name + \
               '生命值：%d\n' % self.hp

def main():
    u = Hero('无敌', 400)
    m1 = Monster('gsy1', 200)
    m2 = Monster('gsy2', 100)
    m3 = Monster('gsy3', 160)
    ms = [m1, m2, m3]
    at_round = 1
    while u.hp > 0 and m1.hp > 0:
        print('===第%d回合===' % at_round)
        u.attack(m1)
        if m1.hp > 0:
            m1.attack(u)
        print(m1)
        print(u)
        at_round += 1
    if u.hp > 0:
        print('%s英雄胜利！' % u.name)
    else:
        print('%s怪兽胜利' )


if __name__ == '__main__':
    main()
