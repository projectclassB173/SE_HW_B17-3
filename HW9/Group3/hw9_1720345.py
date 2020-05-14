import random
class Person(object):
    def __init__(self,name,hp,level):
        self.name = name #名称
        self.max = hp #血槽
        self._hp = hp #血量
        self.level = level #等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return 'Name:{}\t HP: {} \t Level:{}'.format(self.name, self._hp, self.level)

class Hero(Person):
    def __init__(self, name,hp=30,level=1,race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human': #英雄
            self.agile = 0.4
        elif self.race == 'elves': #怪兽
            self.agile = 0.8
    def attack(self,monster):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(5,20)
        elif self.level==3:
            hurt=random.randint(5,30)
        monster.defence(hurt)
    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('命中！你受到{}点伤害'.format(hurt))
        else:
            print('。。。你没有受到攻击！')
    def upgrade(self):
        self.level += 1
        self.max = self.max + 20
        self._hp = self.max
        print('-' * 10, '你成功升级到{}级！血量提升为{}'.format(self.level, self._hp), '-'*10)

class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)
    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)
        hero.defence(hurt)
    def defence(self, hurt):
        self._hp -= hurt
        print('命中！{}受到了{}点伤害'.format(self.name, hurt))
def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 4)
        self.shield = 300   # 护盾
    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)
    def defence(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print("{}受到{}点伤害,当前护盾剩余{}".format(self.name,hurt,self.shield))
        else:
            if self.shield > 0:
                self._hp -= self.shield
                self.shield = 0
                print("{}受到{}点伤害,当前护盾剩余{}".format(self.name,hurt,self.shield))
            else:
                self._hp -= hurt
                print("{}受到{}点伤害,当前护盾剩余{}".format(self.name,hurt,self.shield))

def main():
    hero1 = Hero("英雄", 200, 1, 'human')
    mon1 = Monster("小怪1号")
    mon2 = Monster("小怪2号", 80, 2)
    boss = Boss("大BOSS", 100)
    monster_list = [mon1, mon2, boss]
    r = 1
    while hero1.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*20,'round {}'.format(r),'*'*20)
            hero1.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero1)
                if hero1.get_hp() <= 0:
                    break
            print(hero1)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero1.upgrade()
    if hero1.get_hp() > 0:
        print('{}你通关了'.format(hero1.get_name()))
    else:
        print('{}你输了!请重新挑战吧！'.format(hero1.get_name()))

if __name__ == '__main__':
    main()


#******************** round 1 ********************
# 命中！小怪1号受到了10点伤害
# 。。。你没有受到攻击！
# Name:英雄	 HP: 200 	 Level:1
# Name:小怪1号	 HP: 10 	 Level:1
# ******************** round 2 ********************
# 命中！小怪1号受到了7点伤害
# 。。。你没有受到攻击！
# Name:英雄	 HP: 200 	 Level:1
# Name:小怪1号	 HP: 3 	 Level:1
# ******************** round 3 ********************
# 命中！小怪1号受到了5点伤害
# Name:英雄	 HP: 200 	 Level:1
# Name:小怪1号	 HP: -2 	 Level:1
# ---------- 你成功升级到2级！血量提升为220 ----------
# ******************** round 4 ********************
# 命中！小怪2号受到了20点伤害
# 命中！你受到5点伤害
# Name:英雄	 HP: 215 	 Level:2
# Name:小怪2号	 HP: 60 	 Level:2
# ******************** round 5 ********************
# 命中！小怪2号受到了16点伤害
# 命中！你受到10点伤害
# Name:英雄	 HP: 205 	 Level:2
# Name:小怪2号	 HP: 44 	 Level:2
# ******************** round 6 ********************
# 命中！小怪2号受到了11点伤害
# 。。。你没有受到攻击！
# Name:英雄	 HP: 205 	 Level:2
# Name:小怪2号	 HP: 33 	 Level:2
# ******************** round 7 ********************
# 命中！小怪2号受到了14点伤害
# 命中！你受到14点伤害
# Name:英雄	 HP: 191 	 Level:2
# Name:小怪2号	 HP: 19 	 Level:2
# ******************** round 8 ********************
# 命中！小怪2号受到了8点伤害
# 。。。你没有受到攻击！
# Name:英雄	 HP: 191 	 Level:2
# Name:小怪2号	 HP: 11 	 Level:2
# ******************** round 9 ********************
# 命中！小怪2号受到了6点伤害
# 。。。你没有受到攻击！
# Name:英雄	 HP: 191 	 Level:2
# Name:小怪2号	 HP: 5 	 Level:2
# ******************** round 10 ********************
# 命中！小怪2号受到了5点伤害
# Name:英雄	 HP: 191 	 Level:2
# Name:小怪2号	 HP: 0 	 Level:2
# ---------- 你成功升级到3级！血量提升为240 ----------
# ******************** round 11 ********************
# 大BOSS受到29点伤害,当前护盾剩余271
# 命中！你受到12点伤害
# Name:英雄	 HP: 228 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 12 ********************
# 大BOSS受到11点伤害,当前护盾剩余260
# 。。。你没有受到攻击！
# Name:英雄	 HP: 228 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 13 ********************
# 大BOSS受到16点伤害,当前护盾剩余244
# 命中！你受到28点伤害
# Name:英雄	 HP: 200 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 14 ********************
# 大BOSS受到26点伤害,当前护盾剩余218
# 。。。你没有受到攻击！
# Name:英雄	 HP: 200 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 15 ********************
# 大BOSS受到29点伤害,当前护盾剩余189
# 。。。你没有受到攻击！
# Name:英雄	 HP: 200 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 16 ********************
# 大BOSS受到12点伤害,当前护盾剩余177
# 命中！你受到12点伤害
# Name:英雄	 HP: 188 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 17 ********************
# 大BOSS受到24点伤害,当前护盾剩余153
# 命中！你受到6点伤害
# Name:英雄	 HP: 182 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 18 ********************
# 大BOSS受到12点伤害,当前护盾剩余141
# 命中！你受到21点伤害
# Name:英雄	 HP: 161 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 19 ********************
# 大BOSS受到22点伤害,当前护盾剩余119
# 命中！你受到8点伤害
# Name:英雄	 HP: 153 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 20 ********************
# 大BOSS受到19点伤害,当前护盾剩余100
# 命中！你受到30点伤害
# Name:英雄	 HP: 123 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 21 ********************
# 大BOSS受到8点伤害,当前护盾剩余92
# 命中！你受到23点伤害
# Name:英雄	 HP: 100 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 22 ********************
# 大BOSS受到6点伤害,当前护盾剩余86
# 。。。你没有受到攻击！
# Name:英雄	 HP: 100 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 23 ********************
# 大BOSS受到24点伤害,当前护盾剩余62
# 命中！你受到1点伤害
# Name:英雄	 HP: 99 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 24 ********************
# 大BOSS受到16点伤害,当前护盾剩余46
# 命中！你受到1点伤害
# Name:英雄	 HP: 98 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 25 ********************
# 大BOSS受到25点伤害,当前护盾剩余21
# 。。。你没有受到攻击！
# Name:英雄	 HP: 98 	 Level:3
# Name:大BOSS	 HP: 100 	 Level:4
# ******************** round 26 ********************
# 大BOSS受到24点伤害,当前护盾剩余0
# 命中！你受到1点伤害
# Name:英雄	 HP: 97 	 Level:3
# Name:大BOSS	 HP: 79 	 Level:4
# ******************** round 27 ********************
# 大BOSS受到5点伤害,当前护盾剩余0
# 命中！你受到10点伤害
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: 74 	 Level:4
# ******************** round 28 ********************
# 大BOSS受到11点伤害,当前护盾剩余0
# 。。。你没有受到攻击！
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: 63 	 Level:4
# ******************** round 29 ********************
# 大BOSS受到7点伤害,当前护盾剩余0
# 。。。你没有受到攻击！
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: 56 	 Level:4
# ******************** round 30 ********************
# 大BOSS受到30点伤害,当前护盾剩余0
# 。。。你没有受到攻击！
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: 26 	 Level:4
# ******************** round 31 ********************
# 大BOSS受到25点伤害,当前护盾剩余0
# 。。。你没有受到攻击！
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: 1 	 Level:4
# ******************** round 32 ********************
# 大BOSS受到17点伤害,当前护盾剩余0
# Name:英雄	 HP: 87 	 Level:3
# Name:大BOSS	 HP: -16 	 Level:4
# ---------- 你成功升级到4级！血量提升为260 ----------
# 英雄你通关了
