import random
class Person(object):
    def __init__(self,name,hp,level):
        self.name=name #名称
        self.max=hp #血槽
        self._hp=hp #血量
        self.level=level #等级
        
        def get_name(self):
            return self.name
        
        def get_hp(self):
            return self._hp
            
        def get_level(self):
            return self.level
            
        def attack(self,target):
            raise NotImplementedError
            
        def __str__(self):
            return 'Name:{}\t HP:{}\t Level:{}'.format{self.name,self._hp,self.level)
            

class Hero(Person):
    def __init__(self,name,hp=30,level=1,race='human'):
        super().__init__(name,hp,level)
        self.race=race
        if self.race=='human': #人类
            self.agile=0.4
        elif self.race=='elves': #精灵
            self.agile=0.8
            
    def attack(self,monster):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        monster.defence(hurt)
        
    def defence(self,hurt):
    defend=random.random()
        if df>self.agile:
            self._hp-=hurt
            if self._hp>0:
                print("{}被击中,遭受了{}点攻击,为{}级,血量剩余{}".format(self.name,hurt,self.level,self._hp))
            else:
                print("{}被击中，遭受了{}点攻击,生命值降低为0,已死亡".format(self.name, hurt))
        else:
            print("{}闪避了当前遭受的攻击,为{}级,血量剩余{}".format(self.name,self.level,self._hp))
            
class Monster:
    def __init__(self,name,hp=30,level=1):
        super().__init__(name,hp,level)
    def attack(self,hero):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        hero.defence(hurt)
    def defense(self,hurt):
        self._hp-=hurt
        if self._hp>0:
            print("{}被击中，遭受了{}点攻击,血量剩余{}".format(self.name,hurt,self._hp))
        else:
            print("{}被击中，遭受了{}点攻击,生命值降低为0,已死亡".format(self.name,hurt))

class BigMonster:
    def __init__(self,name,hp=30,level=1):
        super().__init__(name,hp,level)
    def attack(self,hero):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        hero.defence(hurt)
    def defense(self,hurt):
        self._hp-=hurt
        if self._hp>0:
            print("{}被击中，遭受了{}点攻击,血量剩余{}".format(self.name,hurt,self._hp))
        else:
            print("{}被击中，遭受了{}点攻击,生命值降低为0,已死亡".format(self.name,hurt))
            
def main():
    hero=Hero("英雄")
    m1=Monster("怪兽1", 1)
    m2=Monster("怪兽2", 2)
    m3=BigMonster("大怪兽", 3)
    enemy=[m1, m2, m3]
    r=1
    while True:
        print("第{}回合：".format(r))
        enemy[0].defense(hero.attack())   
        if enemy[0]._hp <= 0:   
            print("{}已死亡".format(enemy[0].name))
            del enemy[0]
        if len(enemy) == 0:   
            print("英雄胜利")
            return
        if hero._hp<=0:
            print("英雄失败")
            return 
        r+=1    
        
if __name__ == '__main__':
  main()
