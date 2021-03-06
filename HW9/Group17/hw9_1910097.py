import random as r


class Hero:
    def __init__(self, name):
        self.name = name     # 名字
        self.level = 1       # 等级
        self.max_hp = self.level*20  # 最大生命
        self.current_hp = self.level*20  # 当前生命

    def attack(self):
        atk = r.randint(0, self.level*10-1)
        print("{}发起进攻!".format(self.name))
        return atk           # 传入defense方法

    def upgrade(self):
        self.current_hp += 10
        self.level += 1
        print("{} 升级,当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))


class Human(Hero):            # 人类，继承了英雄的所有属性，攻击和升级方法
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = 0.4        # 灵敏度

    def defense(self, atk):
        is_hurt = r.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")


class Spirit(Hero):           # 精灵，继承了英雄的所有属性，攻击和升级方法
    def __init__(self, name):
        super(Spirit, self).__init__(name)
        self.avd = 0.7        # 灵敏度

    def defense(self, atk):
        is_hurt = r.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")


class Monster:
    def __init__(self, name, level):
        self.name = name      # 名字
        self.level = level    # 等级
        self.max_hp = int(level * 15)  # 最大生命
        self.current_hp = int(level * 15)  # 当前生命

    def attack(self):
        atk = r.randint(0, self.level*10-1)
        print("{} 发起进攻!".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))


class BigMonster(Monster):       # 大怪兽继承了所有怪兽属性，攻击和防御方法，拥有护盾属性并重写防御方法
    def __init__(self, name, level):
        super(BigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  # 护盾值为最大生命的20%

    def defense(self, atk):   # 重写防御方法，受到攻击优先扣除护盾
        if self.shield - atk >= 0:
            self.shield -= atk
            print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))


def main():
    h = Spirit("妖精")   # 生成英雄和怪兽实例
    m1 = Monster("小怪兽一号", 1)
    m2 = Monster("小怪兽二号", 2)
    m3 = BigMonster("大怪兽", 2)
    enemy = [m1, m2, m3]
    r = 1
    while True:
        print("--------Round{}--------".format(r))
        enemy[0].defense(h.attack())   # 每回合英雄先攻击第一个怪兽，必须杀死第一个怪兽才能改变攻击对象
        if enemy[0].current_hp <= 0:   # 如果怪兽阵亡，从列表中删除这个怪兽，英雄升级
            print("{} 阵亡".format(enemy[0].name))
            h.upgrade()
            del enemy[0]
        if len(enemy) == 0:      # 怪兽数量为0，英雄胜利
            print("{} Win!".format(h.name))
            return
        for each in enemy:       # 英雄攻击完后，怪兽轮流攻击英雄
            h.defense(each.attack())
        if h.current_hp <= 0:    # 英雄阵亡，失败
            print("{} Lose!".format(h.name))
            return
        r += 1    # 回合数


if __name__ == '__main__':
    main()

'''
--------Round1--------
妖精发起进攻!
小怪兽一号 受到 3 点伤害,当前血量 12
小怪兽一号 发起进攻!
Miss!
小怪兽二号 发起进攻!
Miss!
大怪兽 发起进攻!
Miss!
--------Round2--------
妖精发起进攻!
小怪兽一号 受到 9 点伤害,当前血量 3
小怪兽一号 发起进攻!
Miss!
小怪兽二号 发起进攻!
妖精 受到 2点伤害,当前血量 18
大怪兽 发起进攻!
妖精 受到 4点伤害,当前血量 14
--------Round3--------
妖精发起进攻!
小怪兽一号 受到 9 点伤害,当前血量 -6
小怪兽一号 阵亡
妖精 升级,当前等级 2,当前血量 24
小怪兽二号 发起进攻!
妖精 受到 4点伤害,当前血量 20
大怪兽 发起进攻!
Miss!
--------Round4--------
妖精发起进攻!
小怪兽二号 受到 19 点伤害,当前血量 11
小怪兽二号 发起进攻!
Miss!
大怪兽 发起进攻!
Miss!
--------Round5--------
妖精发起进攻!
小怪兽二号 受到 12 点伤害,当前血量 -1
小怪兽二号 阵亡
妖精 升级,当前等级 3,当前血量 30
大怪兽 发起进攻!
妖精 受到 17点伤害,当前血量 13
--------Round6--------
妖精发起进攻!
大怪兽 受到 11点伤害,当前护盾值 0 血量 24.0
大怪兽 发起进攻!
Miss!
--------Round7--------
妖精发起进攻!
大怪兽 受到 0点伤害,当前护盾值 0 血量 24.0
大怪兽 发起进攻!
Miss!
--------Round8--------
妖精发起进攻!
大怪兽 受到 13点伤害,当前护盾值 0 血量 11.0
大怪兽 发起进攻!
妖精 受到 11点伤害,当前血量 2
--------Round9--------
妖精发起进攻!
大怪兽 受到 5点伤害,当前护盾值 0 血量 6.0
大怪兽 发起进攻!
Miss!
--------Round10--------
妖精发起进攻!
大怪兽 受到 27点伤害,当前护盾值 0 血量 -21.0
大怪兽 阵亡
妖精 升级,当前等级 4,当前血量 12
妖精 Win!
'''