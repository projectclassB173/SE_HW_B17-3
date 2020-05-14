import random
class Hero:
    def __init__(self, name):
        self.name = name     
        self.level = 1      
        self.max_hp = self.level*24  
        self.current_hp = self.level*24

    def attack(self):
        atk = rn.randint(0, self.level*10-1)    
        print("{}发起进攻!".format(self.name))
        return atk

    def upgrade(self):    
        self.current_hp += 24
        self.level += 1
        print("{} 已升级!当前等级 {}!当前血量 {}".format(self.name, self.level, self.current_hp))

class Human(Hero):
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = 0.4       

    def defense(self, atk):
        is_hurt = rn.random()
        if self.avd < is_hurt:
            self.current_hp -= atk  
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")

class Fairy(Hero):
    def __init__(self, name):
        super(Fairy, self).__init__(name)
        self.avd = 0.7       

    def defense(self, atk):
        is_hurt = rn.random()
        if self.avd < is_hurt:
            self.current_hp -= atk  
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")


class Monster:
    def __init__(self, name, level):
        self.name = name     
        self.level = level    
        self.max_hp = int(level * 24)  
        self.current_hp = int(level * 24)  

    def attack(self):
        atk = rn.randint(0, self.level*10-1)
        print("{} 发起进攻!".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))

class ENDMonster(Monster):
    def __init__(self, name, level):
        super(ENDMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.3  

    def defense(self, atk):  
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
    playerName= "hong"    
    playerRace = input("请选择种族(1、人类 2、精灵)：")
    if playerRace == "1":
        hero = Human(playerName)
    elif playerRace == "2":
        hero = Fairy(playerName)

    m1 = Monster("怪兽1", 1)
    m2 = Monster("怪兽2", 1)
    m3 = ENDMonster("Boss", 2)
    monster = [m1, m2, m3]
    r = 1
    while True:
        print("--------Round{}--------".format(r))
        monster[0].defense(hero.attack())   
        if monster[0].current_hp <= 0:  
            print("{} 阵亡".format(monster[0].name))
            hero.upgrade()  
            del monster[0]  
        if len(monster) == 0:   
            print("{} Win!".format(hero.name))
            return
        for each in monster:    
            hero.defense(each.attack())
        if hero.current_hp <= 0:   
            print("{} Lose!".format(hero.name))
            return
        r += 1  

if __name__ == '__main__':
    main()