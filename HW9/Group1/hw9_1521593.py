import random
class Role:  #该类为英雄和怪兽的父类
    def __init__(self,name):
        self.name=name            #名字
        self.grade=1         #等级
        self.max_live=self.grade*10    #最大生命值
        self.cur_live=self.max_live    #当前生命值

    #攻击方法
    def attack(self):
        print('{}发起了进攻！'.format(self.name))
        ht=random.randint(0,self.grade*10)
        return ht

    #判断是否还活着
    def isLiving(self):
        if self.cur_live>0:
            return True
        else:
            return False

class Monster(Role): #怪兽类，继承自Role
    def __init__(self,name,grade):
        super(Monster,self).__init__(name)
        self.grade=grade  #初始化怪兽可以指定等级
        self.cur_live=grade*10
        if self.grade==3:
            self.shield=30 #如果怪兽等级为3，则初始化一个盾牌属性
        return

    #怪兽防御方法
    def defense(self,ht):
        if self.grade==3:
            if self.shield>0:
                self.shield-=ht
                self.shield=self.shield if self.shield>0 else 0
                print('{}受到{}伤害，当前盾牌防御值{}'.format(self.name,ht,self.shield))
            else:
                self.cur_live-=ht
                print('{}受到了{}点伤害，当前生命值为{}'.format(self.name, ht, self.cur_live))
        else:
            self.cur_live-=ht
            print('{}受到了{}点伤害，当前生命值为{}'.format(self.name,ht,self.cur_live))

#英雄类
class Hero(Role):
    def __init__(self,name,race,live=50): #初始化时可以指定种族,血量默认100
        super(Hero,self).__init__(name)
        self.cur_live=live
        self.race=race
        if self.race=='人类':
            self.flexibility=0.4
        elif self.race=='精灵':
            self.flexibility=0.7

    #升级方法
    def upGrade(self):
        self.grade+=1
        print('{}升级了！当前等级为{}'.format(self.name,self.grade))

    #防御方法
    def defense(self,ht):
        a=random.random()
        if a<self.flexibility:
            print('{}躲避了伤害，当前生命值为{}'.format(self.name,self.cur_live))
        else:
            self.cur_live-=ht
            print('{}受到了{}点伤害，当前生命值为{}'.format(self.name,ht,self.cur_live))

def main():
    hero=Hero('皮卡丘','精灵')
    monster1=Monster('小怪兽1号',1)
    monster2=Monster('小怪兽2号',2)
    monster3=Monster('大怪兽',3)
    monsters=[monster1,monster2,monster3]
    round=1
    while True:
        print('============Round{}=============='.format(round))
        monsters[0].defense(hero.attack())
        if monsters[0].isLiving()==False:
            print('{}阵亡'.format(monsters[0].name))
            hero.upGrade()
            del monsters[0]
        for monster in monsters: #怪兽轮流攻击英雄
            hero.defense(monster.attack())
        if len(monsters)==0: #所有怪兽都已阵亡，英雄胜利！
            print('{} Win!'.format(hero.name))
            break
        if hero.isLiving()==False:
            print('{} Lose!'.format(hero.name))
            break
        round+=1
        print()
    return

if __name__ == '__main__':
    main()
