import random as k

class Hero:
    #属性
    def __init__(hero, name):   #初始函数
        hero.name = name     # 英雄名字
        hero.level = 1       # 英雄等级
        hero.max_hp = hero.level*50  # 英雄最大生命
        hero.current_hp = hero.level*50  # 英雄当前生命
    #攻击函数
    def attack(hero):
        atk = k.randint(0, hero.level*10)
        print("==英雄发动攻击回合==")
        return atk
    #升级函数
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10  #当前血量
        hero.level = hero.level +1
        print("——英雄当前等级 {},当前血量 {}，{}成功升级".format(hero.name, hero.level, hero.current_hp))

class HeroHuman(Hero):
    def __init__(hero, name):      #初等函数
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.6        # 灵活性数值
    #防御函数
    def defense(hero, atk):
        is_hurt = k.random()#产生随机数，如果小于0.4则躲避，大于则命中
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("——人类受到 {}点伤害,当前血量 {}".format(atk, hero.current_hp))
        else:
            print("==人类躲过了攻击==")
# 精灵分支
class HeroSpirit(Hero):
    # 属性函数
    def __init__(hero, name):   #初始函数
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.8        # 灵活性数值

    # 防御函数
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("——精灵受到 {}点伤害,当前血量 {}".format( atk, hero.current_hp))
        else:
            print("==精灵躲过了攻击==")

class Monster:
    #属性
    def __init__(monster, name, level):     #初始函数
        monster.name = name      # 怪兽名字
        monster.level = level    # 怪兽等级
        monster.max_hp = int(level * 40)  # 怪兽最大生命
        monster.current_hp = int(level * 40)  # 怪兽当前生命

    # 攻击函数
    def attack(monster):
        atk = k.randint(0, monster.level * 5)
        print("==怪兽发动攻击回合==".format(monster.name))
        return atk

        # 挨打方法
    def hurt(self, monster):
        self.hp -= monster.damage
        if self.hp > 0:
            print("{2}当前攻击造成的伤害为{3}，"
                "{0}掉血量为{3}，"
                "{0}剩余血量为{1}"
                .format(self.name, self.hp,
                              monster.name, monster.damage))
        else:
         self.hp = 0
         print("{2}当前攻击造成的伤害为{3}，"
                      "{0}掉血量为{3}，"
                      "{0}剩余血量为{1}"
                      .format(self.name, self.hp,
                              monster.name, monster.damage))
        self.death()

        # 防御手段
    def defense(monster, atk):
        monster.current_hp -= atk
        print("怪兽受到 {} 点伤害,当前血量 {}".format( atk, monster.current_hp))

# 怪兽boss函数
class bigMonster(Monster):
    # 属性函数
    def __init__(self, name, level):
        super(bigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  # 护盾值
    # 防御函数
    def defense(self, atk):   # 受到攻击优先扣除护盾
        if self.shield - atk >= 0:
            self.shield = self.shield
            print("——怪兽boss受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("——怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("——怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))


#主方法函数
def main():
    #生成一个英雄，两个低等级怪兽，一个大怪兽
    hero = HeroHuman("人类")
    m1 = Monster("怪兽1号", 1)
    m2 = Monster("怪兽2号", 2)
    m3 = bigMonster("怪兽boss", 3)
    MonsterNum = [m1, m2, m3]
    k = 1
    while True:
        print("==游戏开始==")
        print("第{}回合：".format(k))
        MonsterNum[0].defense(hero.attack())   # 英雄轮番攻击怪兽1,2和怪兽Boss
        if MonsterNum[0].current_hp <= 0:   # 如果怪兽阵亡，从列表中删除这个怪兽，英雄升级
            print("——{} 血量为0阵亡".format(MonsterNum[0].name))
            hero.upgrade()
            del MonsterNum[0]
        if len(MonsterNum) == 0:      # 英雄胜利的条件是怪兽数量为0
            print("==英雄成功打败所有怪兽，取得胜利==")
            return

        for each in MonsterNum:       # 轮流攻击机制
            hero.defense(each.attack())
        if hero.current_hp <= 0:    # 英雄生命值小于等于0则为失败
            print("==英雄攻击失败，导致死亡，请重新开始游戏==")
            return
        k += 1    # 回合数加1
if __name__ == '__main__':
  main()
  print("==游戏结束==")


'''
==游戏开始==
第1回合：
==英雄发动攻击回合==
怪兽受到 1 点伤害,当前血量 39
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
==人类躲过了攻击==
==游戏开始==
第2回合：
==英雄发动攻击回合==
怪兽受到 5 点伤害,当前血量 34
==怪兽发动攻击回合==
——人类受到 2点伤害,当前血量 48
==怪兽发动攻击回合==
——人类受到 8点伤害,当前血量 40
==怪兽发动攻击回合==
——人类受到 1点伤害,当前血量 39
==游戏开始==
第3回合：
==英雄发动攻击回合==
怪兽受到 7 点伤害,当前血量 27
==怪兽发动攻击回合==
——人类受到 0点伤害,当前血量 39
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
==人类躲过了攻击==
==游戏开始==
第4回合：
==英雄发动攻击回合==
怪兽受到 8 点伤害,当前血量 19
==怪兽发动攻击回合==
——人类受到 3点伤害,当前血量 36
==怪兽发动攻击回合==
——人类受到 3点伤害,当前血量 33
==怪兽发动攻击回合==
==人类躲过了攻击==
==游戏开始==
第5回合：
==英雄发动攻击回合==
怪兽受到 7 点伤害,当前血量 12
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
——人类受到 6点伤害,当前血量 27
==怪兽发动攻击回合==
==人类躲过了攻击==
==游戏开始==
第6回合：
==英雄发动攻击回合==
怪兽受到 1 点伤害,当前血量 11
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
——人类受到 7点伤害,当前血量 20
==怪兽发动攻击回合==
——人类受到 6点伤害,当前血量 14
==游戏开始==
第7回合：
==英雄发动攻击回合==
怪兽受到 9 点伤害,当前血量 2
==怪兽发动攻击回合==
——人类受到 0点伤害,当前血量 14
==怪兽发动攻击回合==
==人类躲过了攻击==
==怪兽发动攻击回合==
——人类受到 2点伤害,当前血量 12
==游戏开始==
第8回合：
==英雄发动攻击回合==
怪兽受到 7 点伤害,当前血量 -5
——怪兽1号 血量为0阵亡
——英雄当前等级 精灵,当前血量 2，22成功升级
==怪兽发动攻击回合==
——人类受到 8点伤害,当前血量 14
==怪兽发动攻击回合==
——人类受到 15点伤害,当前血量 -1
==英雄攻击失败，导致死亡，请重新开始游戏==
==游戏结束==
'''
