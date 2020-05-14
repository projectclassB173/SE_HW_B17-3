import random

class Hero:
    def __init__(hero, name):
        hero.name = name     # 名字
        hero.level = 1       # 等级
        hero.max_san = hero.level*100  # 最大san值
        hero.current_san = hero.level*100  # 当前san值

    def attack(hero):
        atk = random.randint(0, hero.level*30)
        print("==调查者发动攻击回合==")
        return atk
    #升级
    def upgrade(hero):
        hero.current_san= hero.current_san+20  #血量
        hero.level = hero.level +1
        print("——调查者当前等级 {},当前san值 {}，{}成功升级".format(hero.name, hero.level, hero.current_san))

class HeroHuman(Hero):
    def __init__(hero, name):      
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.5       
    #防御
    def defense(hero, atk):
        is_hurt = random.random()#闪避
        if hero.avd < is_hurt:
            hero.current_san -= atk
            print("——调查员遭到了 {}点伤害,当前san值 {}".format(atk, hero.current_san))
        else:
            print("==调查员躲过了旧日支配者的攻击==")


class Monster:
    def __init__(monster, name, level):     
        monster.name = name      # 名字
        monster.level = level    # 等级
        monster.max_hp = int(level * 40)  # 最大生命
        monster.current_hp = int(level * 40)  # 当前生命

    # 攻击
    def attack(monster):
        atk = random.randint(0, monster.level * 5)
        print("==旧日支配者发动攻击回合==".format(monster.name))
        return atk

        # 受伤
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

        # 防御
    def defense(monster, atk):
        monster.current_hp -= atk
        print("——旧日支配者到 {} 点伤害,当前血量 {}".format( atk, monster.current_hp))

# 怪兽boss函数
class bigMonster(Monster):
    def __init__(self, name, level):
        super(bigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  # 护盾值
    # 防御
    def defense(self, atk):   #先扣除护盾值
        if self.shield - atk >= 0:
            self.shield = self.shield
            print("——阿撒托斯受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("——阿撒托斯：受到 {}点伤害,当前护盾值 {} 血量 {}".format( atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("——阿撒托斯：受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))


#主函数
def main():
    hero = HeroHuman("调查员")
    m1 = Monster("犹格·索托斯", 1)
    m2 = Monster("克苏鲁", 2)
    m3 = bigMonster("阿撒托斯", 3)
    MonsterNum = [m1, m2, m3]
    k = 1
    while True:
        print("第{}回合：".format(k))
        MonsterNum[0].defense(hero.attack())   
        if MonsterNum[0].current_hp <= 0:   
            print("——{} 被击退".format(MonsterNum[0].name))
            hero.upgrade()
            del MonsterNum[0]
        if len(MonsterNum) == 0:      # 怪兽数量为0调查员胜利
            print("==旧日支配者们被暂时的击退，但他们仍在那黑暗的虚空中等待着卷土重来==")
            return

        for each in MonsterNum:       # 攻击机制
            hero.defense(each.attack())
        if hero.current_san <= 0:    # 英雄失败
            print("==调查员陷入了永久的沉睡之中==")
            return
        k += 1    # 回合数加1
if __name__ == '__main__':
  main()
  print("==游戏结束==")
  '''
第1回合：
第1回合：
==调查者发动攻击回合==
——旧日支配者到 9 点伤害,当前血量 31
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
==旧日支配者发动攻击回合==
——调查员遭到了 5点伤害,当前san值 95
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第2回合：
==调查者发动攻击回合==
——旧日支配者到 18 点伤害,当前血量 13
==旧日支配者发动攻击回合==
——调查员遭到了 3点伤害,当前san值 92
==旧日支配者发动攻击回合==
——调查员遭到了 1点伤害,当前san值 91
==旧日支配者发动攻击回合==
——调查员遭到了 5点伤害,当前san值 86
第3回合：
==调查者发动攻击回合==
——旧日支配者到 1 点伤害,当前血量 12
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
==旧日支配者发动攻击回合==
——调查员遭到了 6点伤害,当前san值 80
==旧日支配者发动攻击回合==
——调查员遭到了 11点伤害,当前san值 69
第4回合：
==调查者发动攻击回合==
——旧日支配者到 19 点伤害,当前血量 -7
——犹格·索托斯 被击退
——调查者当前等级 调查员,当前san值 2，89成功升级
==旧日支配者发动攻击回合==
——调查员遭到了 2点伤害,当前san值 87
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第5回合：
==调查者发动攻击回合==
——旧日支配者到 42 点伤害,当前血量 38
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第6回合：
==调查者发动攻击回合==
——旧日支配者到 7 点伤害,当前血量 31
==旧日支配者发动攻击回合==
——调查员遭到了 0点伤害,当前san值 87
==旧日支配者发动攻击回合==
——调查员遭到了 7点伤害,当前san值 80
第7回合：
==调查者发动攻击回合==
——旧日支配者到 36 点伤害,当前血量 -5
——克苏鲁 被击退
——调查者当前等级 调查员,当前san值 3，100成功升级
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第8回合：
==调查者发动攻击回合==
——阿撒托斯受到 24点伤害,当前护盾值 24.0 血量 120
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第9回合：
==调查者发动攻击回合==
——阿撒托斯：受到 44点伤害,当前护盾值 0 血量 96.0
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第10回合：
==调查者发动攻击回合==
——阿撒托斯：受到 阿撒托斯点伤害,当前护盾值 31 血量 0
==旧日支配者发动攻击回合==
==调查员躲过了旧日支配者的攻击==
第11回合：
==调查者发动攻击回合==
——阿撒托斯：受到 阿撒托斯点伤害,当前护盾值 49 血量 0
==旧日支配者发动攻击回合==
——调查员遭到了 10点伤害,当前san值 90
第12回合：
==调查者发动攻击回合==
——阿撒托斯：受到 阿撒托斯点伤害,当前护盾值 77 血量 0
——阿撒托斯 被击退
——调查者当前等级 调查员,当前san值 4，110成功升级
==旧日支配者们被暂时的击退，但他们仍在那黑暗的虚空中等待着卷土重来==
==游戏结束==

'''
