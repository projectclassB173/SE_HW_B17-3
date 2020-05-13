import time  # 引用时间模块
import random  # 引用随机数模块


class HM():  # 战斗者类
    def __init__(self, name, level=1):  # 初始化函数
        self.name = name
        self.level = level
        self.maxhp = self.level * 100
        self.thp = self.maxhp
        self.avd = -1
        self.sheld = 0

    def attack(self):  # 攻击方法
        time.sleep(1)
        print(f"{self.name}进行攻击!",end=' ')
        A = random.randint(0, self.level * 10)  # 攻击伤害为 0-level*10 的随机数
        time.sleep(1)
        print(f"伤害: {A}")
        time.sleep(1)
        return A

    def defence(self, atk):
        B = random.random()
        if self.sheld - atk >= 0 and atk>0:
            self.sheld -= atk
            print(f"{self.name}受到{atk}点伤害，当前生命值{self.thp}，护盾值{self.sheld}")
        else:
            if self.sheld > 0:
                self.thp -= atk - self.sheld
                self.sheld = 0
                print(f"{self.name}受到{atk}点伤害，当前生命值{self.thp}，护盾值{self.sheld}")
            elif self.avd < B:
                self.thp -= atk
                print(f"{self.name}受到{atk}点伤害，当前生命值{self.thp}")
            else:
                print("MISS！")

    def __str__(self):  # 内置魔法方法,输出对象时输出

        return f"----{self.name}----       HP:{self.thp} "


class Monster(HM):  # 怪兽类 ,继承战斗者类
    def __init__(self, name, level):  # 初始化函数
        super().__init__(name, level)
        self.maxhp = 100
        self.thp=self.maxhp
        if level == 3:
            self.sheld = self.maxhp * 0.2


class hero(HM):  # 英雄类,继承战斗者类
    def __init__(self, name, level=1):
        super().__init__(name, level)

    def setrace(self, race=1):
        if race == 1:
            self.avd = 0.4
        else:
            self.avd = 0.8

    def levelup(self):
        if self.level < 3:
            self.level += 1
            self.maxhp = self.level * 100
            self.thp = self.maxhp
            print(f"{self.name}升级，当前等级{self.level}，当前血量{self.thp}")


def main():  # 执行函数
    num = 0
    A = hero(input("请输入您的英雄名字:   "))
    A.setrace(int(input("1表示人类 2表示精灵请输入你的种族：   ")))
    B = Monster("小怪兽zjd", 1)
    C = Monster("小怪兽css", 1)
    D = Monster("大怪兽yjq", 3)
    monster = [B, C, D]
    while True:
        num += 1
        time.sleep(1)
        print(f"============第{num}回合=============")
        print(A)
        for each in monster:
            print(each)
        attcho = random.randint(0, len(monster) - 1)
        monster[attcho].defence(A.attack())
        if monster[attcho].thp <= 0:
            print(f"{monster[attcho].name}死亡")
            A.levelup()
            del monster[attcho]
        if len(monster) == 0:
            time.sleep(1)
            print("YOU WIN!")
            return True
        for each in monster:
            A.defence(each.attack())
            if A.thp <= 0:
                time.sleep(1)
                print("YOU LOST!")
                return True


if __name__ == '__main__':
    main()
