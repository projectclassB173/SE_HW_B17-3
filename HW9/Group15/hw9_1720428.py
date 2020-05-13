import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = self.level*8000
        self.current_hp = self.level*8000
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
    h = Human("Nonese")
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
        r += 1    

if __name__ == '__main__':
    main()

