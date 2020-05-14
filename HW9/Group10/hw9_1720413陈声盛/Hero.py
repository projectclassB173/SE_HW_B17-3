import random
class Person(object):
    def __init__(self,name,hp,level,shield):
        self.name=name
        self.max=hp #血槽
        self._hp=hp  #血量
        self.level=level
        self.shield = shield

    def get_name(self):
        return self.name
    def get_hp(self):
        return self._hp
    def get_level(self):
        return self.level
    def attack(self,target):
        raise NotImplementedError
    def __str__(self):
        return 'Name:{}\t HP:{}\t Level:{}\t shield:{}'.format(self.name,self._hp,self.level,self.shield)

class Hero(Person):
    def __init__(self,name,hp=30,level=1,race='human',shield=20):
        super().__init__(name,hp,level,shield)
        self.race=race
        if self.race=='1': #人类
            self.agile=0.4
        elif self.race=='2': #精灵
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
        str=random.random()
        if str>=self.agile:
            self.shield -= hurt
            if self.shield <= 0:
                self._hp -= hurt
                print("护盾破裂！")
                print('怪兽向{}攻击\n{}受到{}了攻击！\n'.format(self.get_name(), self.get_name(),hurt))
            else:
                print("护盾受到{}点攻击".format(hurt))
        else:
            print('怪兽向{}攻击，但被{}躲避了攻击！\n'.format(self.get_name(),self.get_name()))

    def upgrade(self):
        if self.level < 3:
            self.level += 1
            self.max=self.max+10
            self.hp=self.max
            print('-'*10,'{}升到了{}级！'.format(self.name, self.level), '-'*10)
        else:
            print("因为{}已满级不能在获得更多的经验值！".format(self.get_name()))