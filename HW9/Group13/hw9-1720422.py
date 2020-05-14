##面向对象编程练习
##编写一个打怪兽的小游戏。
##游戏要求如下：
##1. 游戏中角色有英雄和怪兽两种大类型。
##2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
##3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
##攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
##例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
##英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
##受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
##生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
##4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
##怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
##所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
##被攻击对象即受到次点数的攻击。
##大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
##5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
##直到英雄死亡或所有怪兽被杀死。
##6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

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
        return 'Name:{}\t HP: {} \t Level:{}'.format(self.name, self._hp, self.level)

class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='人类'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == '人类':
            self.agile = 0.4
        elif self.race == '精灵':
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
            print('{}受到了{}点伤害'.format(self.name,hurt))
        else:
            print('{}躲避了攻击'.format(self.name))

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-'*5, '{}升级到{}级,血量提升为{}'.format(self.name,self.level, self._hp), '-'*5)

class Monster(Person):
    def __init__(self, name, hp=15, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('{}受到了{}点伤害'.format(self.name, hurt))


class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp,3)
        self.hudun =20

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        if self.hudun - hurt >= 0:
            self.hudun -= hurt
            print("{}受到{}点伤害,当前护盾剩余{}".format(self.name, hurt, self.hudun))
        else:
            if self.hudun > 0:
                self._hp -= self.hudun
                self.hudun = 0
                print("{}受到{}点伤害,当前护盾剩余{}".format(self.name, hurt, self.hudun))
            else:
                self._hp -= hurt
                print("{}受到{}点伤害,当前护盾剩余{}".format(self.name, hurt, self.hudun))







def main():
    hero = Hero("姜杰", 100, 1, '精灵')
    m1 = Monster("Monster1")
    m2 = Monster("Monster2", 50, 2)
    m3 = Boss("Boss", 70)
    monster_list = [m1, m2, m3]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:


        while monster_list[0].get_hp() > 0:
            print('*'*10, '第{}回合'.format(r), '*'*10)
            hero.attack(monster_list[0])
            if monster_list[0].get_hp() > 0:
                monster_list[0].attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster_list[0])
            r += 1
        if monster_list[0].get_hp() <= 0:
            del monster_list[0]
            hero.upgrade()


    if hero.get_hp() > 0:
        print('{}你胜利了'.format(hero.get_name()))
    else:
        print('{}你输了'.format(hero.get_name()))


if __name__ == '__main__':
    main()