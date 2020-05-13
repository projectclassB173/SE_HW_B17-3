import random as d


class Hero:
    def __init__(self, name):
        self.name = name    
        self.level = 1     
        self.max_hp = self.level*30 
        self.current_hp = self.level*30

    def attack(self):
        atk = d.randint(0, self.level*10-1)
        print("{}发起进攻!".format(self.name))
        return atk        

    def upgrade(self):
        self.current_hp += 10
        self.level += 1
        print("{} 升级,当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))


class Human(Hero):           
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = 0.4     

    def defense(self, atk):
        is_hurt = d.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")


class Spirit(Hero):         
    def __init__(self, name):
        super(Spirit, self).__init__(name)
        self.avd = 0.7        

    def defense(self, atk):
        is_hurt = d.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")


class Monster:
    def __init__(self, name, level):
        self.name = name    
        self.level = level  
        self.max_hp = int(level * 18) 
        self.current_hp = int(level * 18) 

    def attack(self):
        atk = d.randint(0, self.level*18-1)
        print("{} 发起进攻!".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))


class Boss(Monster):     
    def __init__(self, name, level):
        super(Boss, self).__init__(name, level)
        self.shield = self.max_hp * 0.4 

    def defense(self, atk):  
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
    h = Spirit("英雄")
    m1 = Monster("墓王尼特", 1)
    m2 = Monster("阿尔特留斯", 2)
    bm = Boss("乌薪王葛温", 2)
    enemy = [m1, m2, bm]
    d = 1
    while True:
        print("--------Round{}--------".format(d))
        enemy[0].defense(h.attack()) 
        if enemy[0].current_hp <= 0:  
            print("{} 阵亡".format(enemy[0].name))
            h.upgrade()
            del enemy[0]
        if len(enemy) == 0:    
            print("{} Win!".format(h.name))
            return
        for each in enemy:     
            h.defense(each.attack())
        if h.current_hp <= 0:  
            print("{} Lose!".format(h.name))
            return
        d += 1


if __name__ == '__main__':
    main()

