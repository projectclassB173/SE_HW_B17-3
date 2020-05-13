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


import random as ra


class Person(object):
    def __init__(self, name, HP, level):
        self.name = name
        self.max = HP
        self._hp = HP
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

class Monster(Person):
    def __init__(self, name, HP=20, level=1):
        super().__init__(name, HP, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = ra.randint(0, 10)
        if self.level == 2:
            hurt = ra.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('{}受到了{}点伤害'.format(self.name, hurt))


class Boss(Person):
    def __init__(self, name, HP):
        super().__init__(name, HP, 4)
        self.shield = 30

    def attack(self, hero):
        hurt = ra.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print("{}受到{}点伤害,护盾剩余{}".format(self.name, hurt, self.shield))
        else:
            if self.shield > 0:
                self._hp -= self.shield
                self.shield = 0
                print("{}受到{}点伤害,护盾剩余{}".format(self.name, hurt, self.shield))
            else:
                self._hp -= hurt
                print("{}受到{}点伤害,护盾剩余{}".format(self.name, hurt, self.shield))


class Hero(Person):
    def __init__(self, name, HP=30, level=1, race='人类'):
        super().__init__(name, HP, level)
        self.race = race
        if self.race == '人类':
            self.agile = 0.4
        elif self.race == '精灵':
            self.agile = 0.8

    def attack(self, monster):
        if self.level == 1:
            hurt = ra.randint(0, 15)
        elif self.level == 2:
            hurt = ra.randint(15,20)
        elif self.level == 3:
            hurt = ra.randint(30,50)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = ra.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('你受到了{}点伤害'.format(hurt))
        else:
            print('Miss! 躲避了攻击')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-'*10, '你升级到{}级,血量提升为{}'.format(self.level, self._hp), '-'*10)


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


def main():
    hero = Hero("张天乐", 100, 1, '精灵')
    m1 = Monster("小怪1号")
    m2 = Monster("小怪2号", 80, 2)
    boss = Boss("巫妖王", 100)
    monster_list = [m1, m2, boss]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*20, '第{}回合'.format(r), '*'*20)
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
            monster = next_monster(monster_list)

    if hero.get_hp() > 0:
        print('你胜利了！，{}'.format(hero.get_name()))
    else:
        print('你输了...')


if __name__ == '__main__':
    main()

C:\Users\hasee\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/hasee/PycharmProjects/untitled/FPgrowth/GAME.py
******************** 第1回合 ********************
小怪1号受到了15点伤害
Miss! 你躲避了攻击
Name:张天乐	 HP: 100 	 Level:1
Name:小怪1号	 HP: 5 	 Level:1
******************** 第2回合 ********************
小怪1号受到了9点伤害
Name:张天乐	 HP: 100 	 Level:1
Name:小怪1号	 HP: -4 	 Level:1
---------- 你升级到2级,血量提升为110 ----------
******************** 第3回合 ********************
小怪2号受到了15点伤害
你受到了14点伤害
Name:张天乐	 HP: 96 	 Level:2
Name:小怪2号	 HP: 65 	 Level:2
******************** 第4回合 ********************
小怪2号受到了15点伤害
Miss! 你躲避了攻击
Name:张天乐	 HP: 96 	 Level:2
Name:小怪2号	 HP: 50 	 Level:2
******************** 第5回合 ********************
小怪2号受到了17点伤害
Miss! 你躲避了攻击
Name:张天乐	 HP: 96 	 Level:2
Name:小怪2号	 HP: 33 	 Level:2
******************** 第6回合 ********************
小怪2号受到了16点伤害
Miss! 你躲避了攻击
Name:张天乐	 HP: 96 	 Level:2
Name:小怪2号	 HP: 17 	 Level:2
******************** 第7回合 ********************
小怪2号受到了18点伤害
Name:张天乐	 HP: 96 	 Level:2
Name:小怪2号	 HP: -1 	 Level:2
---------- 你升级到3级,血量提升为120 ----------
******************** 第8回合 ********************
巫妖王受到31点伤害,当前护盾剩余0
你受到了21点伤害
Name:张天乐	 HP: 99 	 Level:3
Name:巫妖王	 HP: 70 	 Level:4
******************** 第9回合 ********************
巫妖王受到48点伤害,当前护盾剩余0
Miss! 你躲避了攻击
Name:张天乐	 HP: 99 	 Level:3
Name:巫妖王	 HP: 22 	 Level:4
******************** 第10回合 ********************
巫妖王受到45点伤害,当前护盾剩余0
Name:张天乐	 HP: 99 	 Level:3
Name:巫妖王	 HP: -23 	 Level:4
---------- 你升级到4级,血量提升为130 ----------
你胜利了！，张天乐

进程已结束，退出代码 0
