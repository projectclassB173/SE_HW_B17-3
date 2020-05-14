import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = self.level*8000
        self.current_hp = self.level*8000
        print("{} 当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))

    def upgrade(self):
        self.current_hp += self.max_hp
        self.level += 1
        print("{} 升级了!当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))

    def attack(self):
        atk = random.randint(0, self.level*10000)
        print("{}发起了攻击!".format(self.name))
        return atk

class Human(Hero):            
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = 0.5

    def defense(self, atk):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到了 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")

class Spirit(Hero):           
    def __init__(self, name):
        super(Spirit, self).__init__(name)
        self.avd = 0.6        

    def defense(self, atk):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到了 {}点伤害,当前血量 {}".format(self.name, atk, self.current_hp))
        else:
            print("Miss!")

class Monster:
    def __init__(self, name, level):
        self.name = name      
        self.level = level    
        self.max_hp = int(level * 300)
        self.current_hp = int(level * 300)
        print("{} 当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))

    def attack(self):
        atk = random.randint(0, self.level*10)
        print("{} 发起了攻击!".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到了 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))

class Boss(Monster):       
    def __init__(self, name, level):
        super(Boss, self).__init__(name, level)
        self.shield = self.max_hp * 0.3
    
    def defense(self, atk):   
        if self.shield - atk >= 0:
            self.shield -= atk
            print("{} 受到了 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("{} 受到了 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("{} 受到了 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))

def main():
    h = Human("fky")
    m1 = Monster("monster1", 1)
    m2 = Monster("monster2", 1)
    m3 = Boss("BOSS", 3)
    enemy = [m1, m2, m3]
    r = 1
    while True:
        print("---回合{}---".format(r))
        enemy[0].defense(h.attack())   
        if enemy[0].current_hp <= 0:   
            print("{} 阵亡".format(enemy[0].name))
            h.upgrade()
            del enemy[0]
        if len(enemy) == 0:      
            print("{} 胜利!".format(h.name))
            return
        for each in enemy:       
            h.defense(each.attack())
        if h.current_hp <= 0:    
            print("{} 失败!".format(h.name))
            return
        r = r+1    

if __name__ == '__main__':
    main()

# fky 当前等级 1, 当前血量 8000
# monster1 当前等级 1, 当前血量 300
# monster2 当前等级 1, 当前血量 300
# BOSS 当前等级 3, 当前血量 900
# ---回合1---
# fky发起了攻击!
# monster1 受到了 7716 点伤害, 当前血量 - 7416
# monster1 阵亡
# fky 升级了!当前等级 2, 当前血量 16000
# monster2 发起了攻击!
# Miss!
# BOSS 发起了攻击!
# Miss!
# ---回合2---
# fky发起了攻击!
# monster2 受到了 14550 点伤害, 当前血量 - 14250
# monster2 阵亡
# fky 升级了!当前等级 3, 当前血量 24000
# BOSS 发起了攻击!
# Miss!
# ---回合3---
# fky发起了攻击!
# BOSS 受到了 4047点伤害, 当前护盾值 0 血量 630.0
# BOSS 发起了攻击!
# Miss!
# ---回合4---
# fky发起了攻击!
# BOSS 受到了 5610点伤害, 当前护盾值 0 血量 - 4980.0
# BOSS 阵亡
# fky 升级了!当前等级 4, 当前血量 32000
# fky 胜利!
