from random import randint


class Hero(object):


    def __init__(self, name, hp, avd):

        self._name = name

        self._hp = hp  # 定义英雄的名字、血量、灵敏度

        self._avd = avd

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

    def defense(self, atk):

        is_hurt = r.random()

        if self.avd < is_hurt:

            self.current_hp -= atk

            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))

        else:

            print("Miss!")


    def __str__(self):  # 返回每次调用之后的参数（血量、魔法量、名字）

        return '%s英雄\n' % self._name + \
 \
               '生命值：%d\n' % self._hp


class Monster(object):  # 定义另一个类（怪兽）

    def __init__(self, name, hp):  # 固定起手式

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
        return '%s怪兽\n' % self.name + \
 \
               '生命值：%d\n' % self.hp


def main():  # 最终调用所有的类对象的属性进行动作，最终的命令执行以上的函数及各种方法

    u1 = Hero('人类', 300, 10)

    u2 = Hero('精灵', 500, 15)

    m1 = Monster('怪兽1', 100)

    m2 = Monster('怪兽2', 180)

    m3 = Monster('大怪兽', 360)

    ms = [m1, m2, m3]

    at_round = 1

    while u1.hp > 0 and m1.hp > 0:  # 设定while循环直到要求的条件将其打破

        print('===第%d回合===' % at_round)

        u1.attack(m1)

        if m1.hp > 0:
            m1.attack(u1)

        print(m1)

        print(u1)

        at_round += 1

    if u1.hp > 0:

        print('%s英雄胜利！' % u1.name)

    else:

        print('%s怪兽胜利' % m1.name)

    at_round = 1

    while u1.hp > 0 and m2.hp > 0:  # 设定while循环直到要求的条件将其打破

        print('===第%d回合===' % at_round)

        u1.attack(m2)

        if m2.hp > 0:
            m1.attack(u1)

        print(m2)

        print(u1)

        at_round += 1

    if u1.hp > 0:

        print('%s英雄胜利！' % u1.name)

    else:

        print('%s怪兽胜利' % m2.name)

    at_round = 1

    while u1.hp > 0 and m3.hp > 0:  # 设定while循环直到要求的条件将其打破

        print('===第%d回合===' % at_round)

        u1.attack(m3)

        if m3.hp > 0:
            m1.attack(u1)

        print(m3)

        print(u1)

        at_round += 1

    if u1.hp > 0:

        print('%s英雄胜利！' % u1.name)

    else:

        print('%s怪兽胜利' % m3.name)

if __name__ == '__main__':
    main()
