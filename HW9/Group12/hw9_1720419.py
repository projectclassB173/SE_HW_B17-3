# 面向对象编程练习
# 编写一个打怪兽的小游戏。
# 游戏要求如下： 
# 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。 
#    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#    被攻击对象即受到次点数的攻击。 
#    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name    # 名称
        self.max = hp       # 血槽
        self._hp = hp       # 血量
        self.level = level  # 等级

    def get_name(self):
        return self.name
    def get_hp(self):
        return self._hp
    def get_level(self):
        return self.level
    def attack(self, target):
        raise NotImplementedError
    def __str__(self):
        return '{}（{}级）\t 剩余血量：{} \t '.format(self.name, self.level, self._hp)

class Hero(Person):
    def __init__(self, name, hp, level, race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':   # 人类
            self.agile = 0.4
        elif self.race == 'elves':   # 精灵
            self.agile = 0.8

    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(8, 20)
        elif self.level == 3:
            hurt = random.randint(20, 30)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('你受到了{}点伤害'.format(hurt))
        else:
            print('你成功躲避了攻击!')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 20
        self._hp = self.max
        print('-'*10, '恭喜你！你升级到了{}级，血量上限提升为{}'.format(self.level,self.max))


class Monster(Person):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 6)
        if self.level == 2:
            hurt = random.randint(10, 20)
        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('{}受到了{}点伤害'.format(self.name, hurt))

def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 80   # 护盾

    def attack(self, hero):
        hurt = random.randint(30, 40)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
            print("{}受到{}点伤害".format(self.name, hurt))


def main():
    hero = Hero("黄汝中", 100, 1, 'human')
    monster1 = Monster("飞龙宝宝", 30, 1)
    monster2 = Monster("冰雪精灵", 60, 2)
    boss = Boss("皇家巨人", 100)
    monsterList = [monster1, monster2, boss]
    round = 1
    while hero.get_hp() > 0 and len(monsterList) > 0:

        monster = next_monster(monsterList)
        while monster.get_hp() > 0:
            print('*'*20, 'round {}'.format(round), '*'*20)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster)
            round += 1
        if monster.get_hp() <= 0:
            monsterList.remove(monster)
            hero.upgrade()
            monster = next_monster(monsterList)

    if hero.get_hp() > 0:
        print('恭喜你，胜利了！{}'.format(hero.get_name()))
    else:
        print('很可惜，你输了。请下次再来')

if __name__ == '__main__':
    main()

# D:\1720419\xiangmushizhan\打怪兽\venv\Scripts\python.exe D:/1720419/xiangmushizhan/打怪兽/dgs
# ******************** round 1 ********************
# 飞龙宝宝受到了2点伤害
# 你受到了4点伤害
# 黄汝中（1级）	 剩余血量：96
# 飞龙宝宝（1级）	 剩余血量：28
# ******************** round 2 ********************
# 飞龙宝宝受到了4点伤害
# 你成功躲避了攻击!
# 黄汝中（1级）	 剩余血量：96
# 飞龙宝宝（1级）	 剩余血量：24
# ******************** round 3 ********************
# 飞龙宝宝受到了9点伤害
# 你受到了2点伤害
# 黄汝中（1级）	 剩余血量：94
# 飞龙宝宝（1级）	 剩余血量：15
# ******************** round 4 ********************
# 飞龙宝宝受到了9点伤害
# 你受到了3点伤害
# 黄汝中（1级）	 剩余血量：91
# 飞龙宝宝（1级）	 剩余血量：6
# ******************** round 5 ********************
# 飞龙宝宝受到了9点伤害
# 黄汝中（1级）	 剩余血量：91
# 飞龙宝宝（1级）	 剩余血量：-3
# ---------- 恭喜你！你升级到了2级，血量上限提升为120
# ******************** round 6 ********************
# 冰雪精灵受到了17点伤害
# 你成功躲避了攻击!
# 黄汝中（2级）	 剩余血量：120
# 冰雪精灵（2级）	 剩余血量：43
# ******************** round 7 ********************
# 冰雪精灵受到了10点伤害
# 你成功躲避了攻击!
# 黄汝中（2级）	 剩余血量：120
# 冰雪精灵（2级）	 剩余血量：33
# ******************** round 8 ********************
# 冰雪精灵受到了14点伤害
# 你受到了11点伤害
# 黄汝中（2级）	 剩余血量：109
# 冰雪精灵（2级）	 剩余血量：19
# ******************** round 9 ********************
# 冰雪精灵受到了20点伤害
# 黄汝中（2级）	 剩余血量：109
# 冰雪精灵（2级）	 剩余血量：-1
# ---------- 恭喜你！你升级到了3级，血量上限提升为140
# ******************** round 10 ********************
# 你成功躲避了攻击!
# 黄汝中（3级）	 剩余血量：140
# 皇家巨人（3级）	 剩余血量：100
# ******************** round 11 ********************
# 你成功躲避了攻击!
# 黄汝中（3级）	 剩余血量：140
# 皇家巨人（3级）	 剩余血量：100
# ******************** round 12 ********************
# 你受到了40点伤害
# 黄汝中（3级）	 剩余血量：100
# 皇家巨人（3级）	 剩余血量：100
# ******************** round 13 ********************
# 皇家巨人受到24点伤害
# 你受到了30点伤害
# 黄汝中（3级）	 剩余血量：70
# 皇家巨人（3级）	 剩余血量：76
# ******************** round 14 ********************
# 皇家巨人受到24点伤害
# 你受到了35点伤害
# 黄汝中（3级）	 剩余血量：35
# 皇家巨人（3级）	 剩余血量：52
# ******************** round 15 ********************
# 皇家巨人受到28点伤害
# 你受到了38点伤害
# 很可惜，你输了。请下次再来
