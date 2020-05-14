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
        if self.race == 'human':   # 英雄
            self.agile = 0.4
        elif self.race == 'elves':   # 怪兽
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
        print('-'*10, '恭喜你！你的等级为{}，血量上限提升为{}'.format(self.level,self.max))


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
    hero = Hero("英雄", 100, 1, 'human')
    monster1 = Monster("怪兽1号", 30, 1)
    monster2 = Monster("怪兽2号", 60, 2)
    boss = Boss("大BOSS", 100)
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


# ******************** round 1 ********************
# 怪兽1号受到了2点伤害
# 你受到了3点伤害
# 英雄（1级）	 剩余血量：97
# 怪兽1号（1级）	 剩余血量：28
# ******************** round 2 ********************
# 怪兽1号受到了4点伤害
# 你成功躲避了攻击!
# 英雄（1级）	 剩余血量：97
# 怪兽1号（1级）	 剩余血量：24
# ******************** round 3 ********************
# 怪兽1号受到了9点伤害
# 你受到了2点伤害
# 英雄（1级）	 剩余血量：95
# 怪兽1号（1级）	 剩余血量：15
# ******************** round 4 ********************
# 怪兽1号受到了9点伤害
# 你受到了4点伤害
# 英雄（1级）	 剩余血量：91
# 怪兽1号（1级）	 剩余血量：6
# ******************** round 5 ********************
# 怪兽1号受到了9点伤害
# 英雄（1级）	 剩余血量：91
# 怪兽1号（1级）	 剩余血量：-3
# ---------- 恭喜你！你的等级为2，血量上限提升为120
# ******************** round 6 ********************
# 怪兽2号受到了17点伤害
# 你成功躲避了攻击!
# 英雄（2级）	 剩余血量：120
# 怪兽2号（2级）	 剩余血量：43
# ******************** round 7 ********************
# 怪兽2号受到了10点伤害
# 你成功躲避了攻击!
# 英雄（2级）	 剩余血量：120
# 怪兽2号（2级）	 剩余血量：33
# ******************** round 8 ********************
# 怪兽2号受到了14点伤害
# 你受到了13点伤害
# 英雄（2级）	 剩余血量：107
# 怪兽2号（2级）	 剩余血量：19
# ******************** round 9 ********************
# 怪兽2号受到了20点伤害
# 英雄（2级）	 剩余血量：109
# 怪兽2号（2级）	 剩余血量：-1
# ---------- 恭喜你！你的等级为3，血量上限提升为140
# ******************** round 10 ********************
# 你成功躲避了攻击!
# 英雄（3级）	 剩余血量：140
# 大BOSS（3级）	 剩余血量：100
# ******************** round 11 ********************
# 你成功躲避了攻击!
# 英雄（3级）	 剩余血量：140
# 大BOSS（3级）	 剩余血量：100
# ******************** round 12 ********************
# 你受到了40点伤害
# 英雄（3级）	 剩余血量：100
# 大BOSS（3级）	 剩余血量：100
# ******************** round 13 ********************
# 皇家巨人受到24点伤害
# 你受到了33点伤害
# 英雄（3级）	 剩余血量：67
# 大BOSS（3级）	 剩余血量：76
# ******************** round 14 ********************
# 皇家巨人受到24点伤害
# 你受到了36点伤害
# 英雄（3级）	 剩余血量：31
# 大BOSS（3级）	 剩余血量：52
# ******************** round 15 ********************
# 大BOSS受到28点伤害
# 你受到了38点伤害
# 很可惜，你输了。请下次再来
