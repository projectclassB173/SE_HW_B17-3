import random as a


class Hero:
    def __init__(self, name):
        self.name = name    
        self.level = 1     
        self.max_hp = self.level*30 
        self.current_hp = self.level*30


    def attack(self):
        atk = a.randint(0, self.level*10-1)
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
        is_hurt = a.random()
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
        is_hurt = a.random()
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
        atk = a.randint(0, self.level*18-1)
        print("{} 发起进攻!".format(self.name))
        return atk


    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))




class BigMonster(Monster):     
    def __init__(self, name, level):
        super(BigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2 


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
    h = Spirit("主角")
    m1 = Monster("小怪a", 1)
    m2 = Monster("小怪b", 2)
    bm = BigMonster("老大", 2)
    enemy = [m1, m2, bm]
    a = 1
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
	
	
--------Round1--------
主角发起进攻!
小怪a 受到 1 点伤害,当前血量 17
小怪a 发起进攻!
Miss!
小怪b 发起进攻!
Miss!
老大 发起进攻!
主角 受到 8点伤害,当前血量 22
--------Round2--------
主角发起进攻!
小怪a 受到 3 点伤害,当前血量 14
小怪a 发起进攻!
Miss!
小怪b 发起进攻!
Miss!
老大 发起进攻!
Miss!
--------Round3--------
主角发起进攻!
小怪a 受到 8 点伤害,当前血量 6
小怪a 发起进攻!
Miss!
小怪b 发起进攻!
Miss!
老大 发起进攻!
Miss!
--------Round4--------
主角发起进攻!
小怪a 受到 7 点伤害,当前血量 -1
小怪a 阵亡
主角 升级,当前等级 2,当前血量 32
小怪b 发起进攻!
Miss!
老大 发起进攻!
Miss!
--------Round5--------
主角发起进攻!
小怪b 受到 10 点伤害,当前血量 26
小怪b 发起进攻!
Miss!
老大 发起进攻!
Miss!
--------Round6--------
主角发起进攻!
小怪b 受到 14 点伤害,当前血量 12
小怪b 发起进攻!
Miss!
老大 发起进攻!
主角 受到 7点伤害,当前血量 25
--------Round7--------
主角发起进攻!
小怪b 受到 2 点伤害,当前血量 10
小怪b 发起进攻!
Miss!
老大 发起进攻!
Miss!
--------Round8--------
主角发起进攻!
小怪b 受到 14 点伤害,当前血量 -4
小怪b 阵亡
主角 升级,当前等级 3,当前血量 35
老大 发起进攻!
主角 受到 25点伤害,当前血量 10
--------Round9--------
主角发起进攻!
老大 受到 21点伤害,当前护盾值 0 血量 28.8
老大 发起进攻!
主角 受到 1点伤害,当前血量 9
--------Round10--------
主角发起进攻!
老大 受到 13点伤害,当前护盾值 0 血量 15.8
老大 发起进攻!
Miss!
--------Round11--------
主角发起进攻!
老大 受到 5点伤害,当前护盾值 0 血量 10.8
老大 发起进攻!
Miss!
--------Round12--------
主角发起进攻!
老大 受到 17点伤害,当前护盾值 0 血量 -6.199999999999999
老大 阵亡
主角 升级,当前等级 4,当前血量 19
主角 Win!
>>> 

