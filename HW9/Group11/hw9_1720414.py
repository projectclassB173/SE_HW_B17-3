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

def select():
    i = input("请选择你的种族（1为人类，2为妖精）：")
    if i==1:
       
       h = Human("人类")
       
    elif i==2:
       h=Spirit("妖精")
    return h

def main():
    select()
    global h
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
