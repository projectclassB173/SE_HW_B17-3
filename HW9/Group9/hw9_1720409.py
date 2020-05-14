import random
from random import randint


class Person(object): #Hero类
    def __init__(self,name,hp,level):
        self.name=name #姓名
        self.max=hp #血槽
        self._hp=hp  #血量
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
        return 'Name:{}\t HP:{}\t Level:{}'.format(self.name,self._hp,self.level)

class Hero(Person):
    def __init__(self,name,hp=30,level=1,race='human'):
        super().__init__(name,hp,level)
        self.race=race
        if self.race=='human': #人类
            self.agile=0.4
        elif self.race=='elves': #精灵
            self.agile=0.8
    def attack(self,monster): #攻击技能，根据角色的level随机造成一定的伤害
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        monster.defence(hurt)

    def defence(self,hurt):  #防御，根据灵活性，具有一定机会躲避攻击
        luck=random.random()
        if luck>=self.agile:
            self._hp -= hurt
            print('你受到{}了攻击！'.format(hurt))
        else:
            print('你躲避了攻击！')

    def upgrade(self):  #升级英雄到下一级，更新血槽，回复hp

        self.level += 1
        self.max=self.max+10
        self.hp=self.max
        print('-'*10,'你升到了{}级！'.format(self.level))

class Monster(Person): #Monster类
        def __init__(self, name, hp=20, level=1):
            super().__init__(name, hp, level)

        def attack(self, hero):
            if self.level == 1:
                hurt = randint(0, 10)
            if self.level == 2:
                hurt = randint(0, 20)
            hero.defence(hurt)

        def defence(self, hurt):
            self._hp -= hurt
            print('怪兽受到{}点伤害'.format(hurt))

class Boss(Person):
        def __init__(self, name, hp):
            super().__init__(name, hp, 3)
            self.shield = 30  # 盾牌

        def attack(self, hero):
            hurt = randint(0, 30)
            hero.defence(hurt)

        def defence(self, hurt):
            self.shield -= hurt
            if self.shield <= 0:
                self._hp -= hurt
            print('Boss受到{}点伤害'.format(hurt))

def main():
        hero = Hero('噬魂蚁王', 100, 1, 'human')
        montser1 = Monster('魔音蝙蝠')
        montser2 = Monster('紫尾貂', 80, 1)
        boss = Boss('七翼暗金蝠王', 100)
        montser_list = [montser1, montser2, boss]
        round = 1
        while hero.get_hp() > 0 and len(montser_list) > 0:
            monster = next_monster(montser_list)
            while monster.get_hp() > 0:
                print('*' * 20, 'fighting of round {}'.format(round), '*' * 20)
                hero.attack(monster)
                if monster.get_hp() > 0:
                    monster.attack(hero)
                    if hero.get_hp() <= 0:
                        break
                print(hero)
                print(monster)
                round += 1
            if monster.get_hp() <= 0:
                montser_list.remove(monster)
                hero.upgrade()
                monster = next_monster(montser_list)
            if hero.get_hp() > 0:
                print('You win,{}'.format(hero.get_name()))
            else:
                print('You lose')

def next_monster(monster_list: list):

        assert type(monster_list) is list
        if len(monster_list) > 0:
           return monster_list[0]

if __name__ == '__main__':
        main()

#结果
'''
******************** fighting of round 1 ********************
怪兽受到2点伤害
你受到6了攻击！
Name:噬魂蚁王	 HP:94	 Level:1
Name:魔音蝙蝠	 HP:18	 Level:1
******************** fighting of round 2 ********************
怪兽受到6点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:94	 Level:1
Name:魔音蝙蝠	 HP:12	 Level:1
******************** fighting of round 3 ********************
怪兽受到4点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:94	 Level:1
Name:魔音蝙蝠	 HP:8	 Level:1
******************** fighting of round 4 ********************
怪兽受到8点伤害
Name:噬魂蚁王	 HP:94	 Level:1
Name:魔音蝙蝠	 HP:0	 Level:1
---------- 你升到了2级！
You win,噬魂蚁王
******************** fighting of round 5 ********************
怪兽受到20点伤害
你受到5了攻击！
Name:噬魂蚁王	 HP:89	 Level:2
Name:紫尾貂	 HP:60	 Level:1
******************** fighting of round 6 ********************
怪兽受到6点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:89	 Level:2
Name:紫尾貂	 HP:54	 Level:1
******************** fighting of round 7 ********************
怪兽受到18点伤害
你受到5了攻击！
Name:噬魂蚁王	 HP:84	 Level:2
Name:紫尾貂	 HP:36	 Level:1
******************** fighting of round 8 ********************
怪兽受到20点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:84	 Level:2
Name:紫尾貂	 HP:16	 Level:1
******************** fighting of round 9 ********************
怪兽受到16点伤害
Name:噬魂蚁王	 HP:84	 Level:2
Name:紫尾貂	 HP:0	 Level:1
---------- 你升到了3级！
You win,噬魂蚁王
******************** fighting of round 10 ********************
Boss受到20点伤害
你受到5了攻击！
Name:噬魂蚁王	 HP:79	 Level:3
Name:七翼暗金蝠王	 HP:100	 Level:3
******************** fighting of round 11 ********************
Boss受到19点伤害
你受到19了攻击！
Name:噬魂蚁王	 HP:60	 Level:3
Name:七翼暗金蝠王	 HP:81	 Level:3
******************** fighting of round 12 ********************
Boss受到2点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:60	 Level:3
Name:七翼暗金蝠王	 HP:79	 Level:3
******************** fighting of round 13 ********************
Boss受到22点伤害
你受到16了攻击！
Name:噬魂蚁王	 HP:44	 Level:3
Name:七翼暗金蝠王	 HP:57	 Level:3
******************** fighting of round 14 ********************
Boss受到8点伤害
你受到7了攻击！
Name:噬魂蚁王	 HP:37	 Level:3
Name:七翼暗金蝠王	 HP:49	 Level:3
******************** fighting of round 15 ********************
Boss受到24点伤害
你受到27了攻击！
Name:噬魂蚁王	 HP:10	 Level:3
Name:七翼暗金蝠王	 HP:25	 Level:3
******************** fighting of round 16 ********************
Boss受到1点伤害
你躲避了攻击！
Name:噬魂蚁王	 HP:10	 Level:3
Name:七翼暗金蝠王	 HP:24	 Level:3
******************** fighting of round 17 ********************
Boss受到10点伤害
你受到6了攻击！
Name:噬魂蚁王	 HP:4	 Level:3
Name:七翼暗金蝠王	 HP:14	 Level:3
******************** fighting of round 18 ********************
Boss受到11点伤害
你受到1了攻击！
Name:噬魂蚁王	 HP:3	 Level:3
Name:七翼暗金蝠王	 HP:3	 Level:3
******************** fighting of round 19 ********************
Boss受到23点伤害
Name:噬魂蚁王	 HP:3	 Level:3
Name:七翼暗金蝠王	 HP:-20	 Level:3
---------- 你升到了4级！
You win,噬魂蚁王   
'''
