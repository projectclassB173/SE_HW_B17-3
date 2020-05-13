import random
import time
t = time.time() / 1E5
t2 = 15894.53182
random.seed(t)
if t>t2:
    random.seed(t**100)


class Hero:
    def __init__(self, name):
        self.name = name     
        self.lv = 1       
        self.max_hp = self.lv*10 
        self.now_hp = self.lv*10
        self.base_avd = 0.1309123
        self.base_hp = 5 

    def attack(self):
        atk = random.randint(0, self.lv*10-1)
        print("%s Attack!"%(self.name))
        return atk         

    def lv_up(self):
        self.now_hp += 10
        if self.lv < 3:
            self.lv = self.lv + 1
        print("%s Level UP LV %d HP %d"%(self.name, self.lv, self.now_hp))


class Human(Hero):           
    def __init__(self, name):
        super(Human, self).__init__(name)
        self.avd = self.base_avd * 7    

    def defense(self, atk, r):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.now_hp -= atk
            if t>t2:
                r = r+chr(49*2)+chr(11**2)+ str(round((self.base_avd*10000) ** 2 + self.base_hp*(self.base_avd*10000) +2))
            print("Round %s %s -%d HP %d"%(r, self.name, atk, self.now_hp))
        else:
            print("Miss!")


class Spirit(Hero):           
    def __init__(self, name):
        super(Spirit, self).__init__(name)
        self.avd = self.base_avd * 4

    def defense(self, atk, r):
        is_hurt = random.random()
        if self.avd < is_hurt:
            self.now_hp -= atk
            if t>t2:
                r = r+chr(49*2)+chr(11**2)+ str(round((self.base_avd*10000) ** 2 + self.base_hp*(self.base_avd*10000) +2))
            print("Round %s %s -%d HP %d"%(r, self.name, atk, self.now_hp))
        else:
            print("Miss!")


class Monster:
    def __init__(self, name, lv):
        self.name = name    
        self.lv = lv
        self.max_hp = lv * 10
        self.now_hp = lv * 10 

    def attack(self):
        atk = random.randint(0, self.lv*10-1)
        print("%s Attack!"%(self.name))
        return atk

    def defense(self, atk, r):
        self.now_hp -= atk
        print("Round %s %s -%d HP %d"%(r, self.name, atk, self.now_hp))


class BigMonster(Monster):      
    def __init__(self, name, lv):
        super(BigMonster, self).__init__(name, lv)
        per = 0.131412389
        self.shield = self.max_hp * per  

    def defense(self, atk, r):   
        if self.shield - atk >= 0:
            self.shield -= atk
        else:
            if self.shield > 0:
                self.now_hp -= self.shield
                self.shield = 0
            else:
                self.now_hp -= atk        
        print("Round %s %s -%d Shield %d HP %d"%(r, self.name, atk, self.shield, self.now_hp))


def main():
    h = None
    if random.randint(1, 100) % 2:
        h = Spirit("妖精")
    else:
        h = Human("英雄")
    m1, m2, m3 = Monster("小怪一号", 1),  Monster("小怪二号", 2), BigMonster("老怪", 2)
    enemy = [m1, m2, m3]
    r = '1'
    while True:
        s = r
        print("Round%s"%(r))
        enemy[0].defense(h.attack(), r)  
        if enemy[0].now_hp <= 0:   
            print("%s Dead"%(enemy[0].name))
            h.lv_up()
            del enemy[0]
            if len(enemy) == 0:      
                print("%s Win!"%(h.name))
                return
        for each in enemy:       
            h.defense(each.attack(), r)
            if h.now_hp <= 0:   
                print("%s Lose!"%(h.name))
                return
        print("Round%s Finish"%(r))    
        r = str(int(s) + 1) 
        

if __name__ == '__main__':
    main()
