#实现不了攻击护盾部分
import random
class hero:
    def __init__(self,name,lv,race, maxblood ):
        self.name = name
        self.lv = lv
        self.maxblood = maxblood
        self.blood = maxblood
        self.race = race
        #种族决定灵活性
        if self.race == '人类':
            self.flexibility = 0.2
        else :
            self.flexibility = 0.4
    #攻击
    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = random.randint(0, 10)
            elif self.lv == 2:
                self.att = random.randint(0, 20)
            elif self.lv == 3:
                self.att = random.randint(0, 30)
            print(self.att)
            beattacked.minus_blood(self.att)
        print(beattacked.name + ' 剩余血量:' + str(beattacked.blood) +'剩余护盾：' + str(beattacked.shield))
        print('--英雄攻击结束--\n')
    # 输出剩余血量
    def minus_blood(self, num):
        self.blood -= num
    #判断死亡
    def has_living(self):
        if self.blood > 0:
            return True
        return False
class monster:
    def __init__(self, name,lv,maxblood,shield):
        self.name = name
        self.lv = lv
        self.maxblood = maxblood
        self.blood = maxblood
        self.blood = self.maxblood
        self.shield = shield

    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = random.randint(0, 10)
            elif self.lv == 2:
                self.att = random.randint(0, 20)
            elif self.lv == 3:
                self.att = random.randint(0, 30)
            print(self.att)
            #判断闪避
            if beattacked.flexibility < random.random():
                beattacked.minus_blood(self.att)
            else:
                beattacked.minus_blood(0)
                print('闪避了攻击')
        print(beattacked.name + ' 剩余血量:' + str(beattacked.blood))
        print('--怪物攻击结束--\n')
    # 输出剩余血量
    def minus_blood(self, num):
        self.blood -= num
    # 判断死亡
    def has_living(self):
        if self.blood > 0:
            return True
        return False
# 创建怪兽
m1 = monster(name='怪兽一号' , lv=1 , maxblood=5 , shield=0)
m2 = monster(name='怪兽二号' , lv=2 , maxblood=10 , shield=0)
m3 = monster(name='怪兽三号' , lv=3 , maxblood=15 , shield=10)
mo = [m1,m2,m3]
# 创建英雄
h = hero(name='英雄甲' , lv=2 , race='人类',maxblood=50)
for m in mo:
    print('------------------------------------------战斗开始-------------------------------------------\n战斗人物信息:')
    print(h.name + '血量：' + str(h.blood))
    print(m.name + '血量:' + str(m.maxblood) + '护盾:' + str(m.shield))
    while m.has_living() and h.has_living():
        print(h.name + ' 对 ' + m.name + ' 造成伤害:')
        h.attack(m)
        if m.has_living():
            print(m.name + ' 对 ' + h.name + ' 造成伤害:')
            m.attack(h)
        else:
            print('怪兽血量非正数，已死亡，无法发动本次回合攻击')

    if h.has_living():
        print(h.name + ' 胜利!\n')
    else:
        print(m.name + ' 胜利!\n')