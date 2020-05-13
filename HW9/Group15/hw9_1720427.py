"""编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
"""
import random as rn  #引入随机数
#英雄类，可选种族：人类和精灵
class Hero:
    def __init__(self, name):
        self.name = name     # 名字
        self.level = 1       # 等级默认为1 一共为3级
        self.max_hp = self.level*30  # 当前等级的最大生命，最大生命根据级数来进行改变
        self.current_hp = self.level*30  # 当前生命

    def attack(self):
        atk = rn.randint(0, self.level*10-1)    #级别为1在[0,10)范围内随机产生一个数作为攻击力
                                                #级别为2在[0, 20)范围内产生一个数作为攻击力
        print("{}发起进攻!".format(self.name))
        return atk

    def upgrade(self):     #杀怪成功后英雄等级和血量相应添加
        self.current_hp += 10
        self.level += 1
        print("{} 升级,当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))


# 人类，继承了英雄的所有属性，攻击和升级方法
class Human(Hero):
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = 0.4        #人类的灵活度为0.4

    def defense(self, atk):
        is_hurt = rn.random()
        if self.avd < is_hurt:
            self.current_hp -= atk  #如果灵敏度小于随机数，无法躲开
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")

# 精灵，继承了英雄的所有属性，攻击和升级方法
class Fairy(Hero):
    def __init__(self, name):
        super(Fairy, self).__init__(name)
        self.avd = 0.7        # 精灵的灵活度为0.7

    def defense(self, atk):
        is_hurt = rn.random()
        if self.avd < is_hurt:
            self.current_hp -= atk  #如果灵敏度小于随机数，无法躲开
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
        atk = rn.randint(0, self.level*10-1)
        print("{} 发起进攻!".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))

#大Boss继承了怪物类中所有属性，增加了额外的盾牌属性
class BigMonster(Monster):
    def __init__(self, name, level):
        super(BigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.3  # 设置护盾值为最大生命的30%

    def defense(self, atk):   # 重写防御方法，受到攻击优先扣除护盾
        if self.shield - atk >= 0:
            self.shield -= atk
            print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
        else:  #当伤害超出护盾值时
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))


def main():
    playerName= "kyf"    # 生成英雄和怪兽实例
    playerRace = input("请选择种族(1、人类 2、精灵)：")
    if playerRace == "1":
        hero = Fairy(playerName)
    elif playerRace == "2":
        hero = Human(playerName)
    m1 = Monster("怪兽小兵一号", 1)
    m2 = Monster("怪兽小兵二号", 2)
    m3 = BigMonster("大Boss", 2)
    monster = [m1, m2, m3]
    r = 1
    while True:
        print("--------Round{}--------".format(r))
        monster[0].defense(hero.attack())   # 每回合英雄先攻击第一个怪兽，必须杀死第一个怪兽才能改变攻击对象
        if monster[0].current_hp <= 0:   # 当怪兽血量不足
            print("{} 阵亡".format(monster[0].name))
            hero.upgrade()  #英雄升级
            del monster[0]  #从列表中删除这个怪兽
        if len(monster) == 0:      # 怪兽数量为0，英雄胜利
            print("{} Win!".format(hero.name))
            return
        for each in monster:       # 英雄攻击完后，怪兽轮流攻击英雄
            hero.defense(each.attack())
        if hero.current_hp <= 0:    # 英雄阵亡，失败
            print("{} Lose!".format(hero.name))
            return
        r += 1    # 回合数

if __name__ == '__main__':
    main()

""""
D:\Program Files\PyCharm 2020.1.1\workspace\Scripts\python.exe" "D:/Program Files/PyCharm 2020.1.1/Projects/hw9_1720427.py"
请选择种族(1、人类 2、精灵)：1
--------Round1--------
kyf发起进攻!
怪兽小兵一号 受到 2 点伤害,当前血量 13
怪兽小兵一号 发起进攻!
Miss!
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
Miss!
--------Round2--------
kyf发起进攻!
怪兽小兵一号 受到 8 点伤害,当前血量 5
怪兽小兵一号 发起进攻!
kyf 受到 3点伤害,当前血量 27
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
Miss!
--------Round3--------
kyf发起进攻!
怪兽小兵一号 受到 3 点伤害,当前血量 2
怪兽小兵一号 发起进攻!
kyf 受到 6点伤害,当前血量 21
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
kyf 受到 3点伤害,当前血量 18
--------Round4--------
kyf发起进攻!
怪兽小兵一号 受到 2 点伤害,当前血量 0
怪兽小兵一号 阵亡
kyf 升级,当前等级 2,当前血量 28
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
Miss!
--------Round5--------
kyf发起进攻!
怪兽小兵二号 受到 7 点伤害,当前血量 23
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
kyf 受到 2点伤害,当前血量 26
--------Round6--------
kyf发起进攻!
怪兽小兵二号 受到 10 点伤害,当前血量 13
怪兽小兵二号 发起进攻!
Miss!
大Boss 发起进攻!
kyf 受到 6点伤害,当前血量 20
--------Round7--------
kyf发起进攻!
怪兽小兵二号 受到 12 点伤害,当前血量 1
怪兽小兵二号 发起进攻!
kyf 受到 13点伤害,当前血量 7
大Boss 发起进攻!
kyf 受到 2点伤害,当前血量 5
--------Round8--------
kyf发起进攻!
怪兽小兵二号 受到 0 点伤害,当前血量 1
怪兽小兵二号 发起进攻!
kyf 受到 3点伤害,当前血量 2
大Boss 发起进攻!
Miss!
--------Round9--------
kyf发起进攻!
怪兽小兵二号 受到 15 点伤害,当前血量 -14
怪兽小兵二号 阵亡
kyf 升级,当前等级 3,当前血量 12
大Boss 发起进攻!
Miss!
--------Round10--------
kyf发起进攻!
大Boss 受到 29点伤害,当前护盾值 0 血量 21.0
大Boss 发起进攻!
kyf 受到 18点伤害,当前血量 -6
kyf Lose!
"""