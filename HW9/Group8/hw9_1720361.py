import random as r

class Hero:
    def __init__(hero, name):
        hero.name = name
        hero.level = 1
        hero.max_hp = hero.level*40
        hero.n_hp = hero.level*40
    def attack(hero):
        attack = r.randint(0, hero.level*20)
        print("英雄发动攻击!")
        return attack
    def uplevel(hero):
        hero.n_hp += 10
        hero.level += 1
        print("{}升级,目前等级：{} , 当前血量：{}".format(hero.name, hero.level, hero.n_hp))

class Human(Hero):
    def __init__(human, name):
        super(Human, human).__init__(name)
        human.avd = 0.4
    def defense(human, attack):
        is_hurt = r.random()
        if human.avd < is_hurt:
            human.n_hp -= attack
            print("人类：受到伤害值：{} , 目前血量：{}".format(attack, human.n_hp))
        else:
            print("Miss!")

class elf(Hero):
    def __init__(elf, name):
        super(elf, elf).__init__(name)
        elf.avd = 0.7
    def defense(elf, attack):
        is_hurt = r.random()
        if elf.avd < is_hurt:
            elf.n_hp -= attack
            print("精灵：受到伤害值：{} , 当前血量：{}".format( attack, elf.n_hp))
        else:
            print("Miss!")


class Monster:
    def __init__(Monster, name, level):
        Monster.name = name
        Monster.level = level
        Monster.max_hp = int(level * 15)
        Monster.n_hp = int(level * 15)
    def attack(Monster):
        attack = r.randint(0, Monster.level * 10)
        print("怪兽发动攻击!")
        return attack
    def defense(Monster, attack):
        Monster.n_hp -= attack
        print("怪兽: 受到伤害值：{} , 当前血量：{}".format( attack, Monster.n_hp))


class BossMonster(Monster):
    def __init__(Monster_Boss, name, level):
        super(BossMonster, Monster_Boss).__init__(name, level)
        Monster_Boss.shield = Monster_Boss.max_hp * 0.5
    def defense(Monster_Boss, attack):
        if Monster_Boss.shield - attack >= 0:
            Monster_Boss.shield = attack - Monster_Boss.shield
            print("大怪兽Boss：受到伤害值：{} , 当前护盾值：{} , 当前血量：{}".format( attack, Monster_Boss.shield, Monster_Boss.n_hp))
        else:
            if Monster_Boss.shield > 0:
                Monster_Boss.n_hp -= Monster_Boss.shield
                Monster_Boss.shield = 0
                print("大怪兽Boss：受到伤害值：{} , 当前护盾值：{} ，当前血量：{}".format( attack, Monster_Boss.shield, Monster_Boss.n_hp))
            else:
                Monster_Boss.n_hp -= attack
                print("大怪兽Boss：受到伤害值：{} , 当前护盾值：{} ，当前血量：{}".format(attack, Monster_Boss.shield, Monster_Boss.n_hp))


def main():
    hero = Human("人类")
    a = Monster("1级小怪兽", 1)
    b = Monster("2级小怪兽", 2)
    c = BossMonster("大怪兽Boss", 3)
    MonsterNum = [a, b, c]
    r = 1
    while True:
        print("=============Round{}=============".format(r))
        MonsterNum[0].defense(hero.attack())
        if MonsterNum[0].n_hp <= 0:
            print("{}阵亡".format(MonsterNum[0].name))
            hero.uplevel()
            del MonsterNum[0]
        if len(MonsterNum) == 0:
            print("英雄：Victory!")
            return

        for each in MonsterNum:
            hero.defense(each.attack())
        if hero.n_hp <= 0:  
            print("英雄：Defeat!")
            return
        r += 1

if __name__ == '__main__':
  main()




=============Round1=============
英雄发动攻击!
怪兽: 受到伤害值：12 , 当前血量：3
怪兽发动攻击!
Miss!
怪兽发动攻击!
人类：受到伤害值：15 , 目前血量：25
怪兽发动攻击!
人类：受到伤害值：4 , 目前血量：21
=============Round2=============
英雄发动攻击!
怪兽: 受到伤害值：20 , 当前血量：-17
1级小怪兽阵亡
人类升级,目前等级：2 , 当前血量：31
怪兽发动攻击!
人类：受到伤害值：13 , 目前血量：18
怪兽发动攻击!
人类：受到伤害值：6 , 目前血量：12
=============Round3=============
英雄发动攻击!
怪兽: 受到伤害值：38 , 当前血量：-8
2级小怪兽阵亡
人类升级,目前等级：3 , 当前血量：22
怪兽发动攻击!
Miss!
=============Round4=============
英雄发动攻击!
大怪兽Boss：受到伤害值：39 , 当前护盾值：0 ，当前血量：22.5
怪兽发动攻击!
人类：受到伤害值：22 , 目前血量：0
英雄：Defeat!