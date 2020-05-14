import random as r

class Hero:
    def __init__(hero, name):
        hero.name = name
        hero.level = 1
        hero.max_hp = hero.level*30
        hero.now_hp = hero.level*30
    def attack(hero):
        a = r.randint(0, hero.level*10)
        print("{}发动攻击!".format(hero.name))
        return a
    def up(hero):
        hero.level = hero.level +1
        hero.now_hp= hero.max_hp
        print("{} 升级,血量恢复最大值，目前等级 {},目前血量 {}".format(hero.name, hero.level, hero.now_hp))

class Human(Hero):
    def __init__(hero, name):
        super(Human, hero).__init__(name)
        hero.avd = 0.4
    def damage(hero, a):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.now_hp -= a
            print("人类受到 {}点伤害,目前血量 {}".format(a, hero.now_hp))
        else:
            print("人类避开了攻击!")


class Elf(Hero):
    def __init__(hero, name):
        super(Elf, hero).__init__(name)
        hero.avd = 0.6
    def damage(hero, a):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.now_hp -= a
            print("精灵受到 {}点伤害,目前血量 {}".format( a, hero.now_hp))
        else:
            print("精灵避开了攻击!")


class Monster:
    def __init__(monster, name, level):
        monster.name = name
        monster.level = level
        monster.max_hp = int(level * 10)
        monster.now_hp = int(level * 10)
    def attack(monster):
        atk = r.randint(0, monster.level * 10)
        print("{}发动攻击!".format(monster.name))
        return atk
    def damage(monster, a):
        monster.now_hp -= a
        print("{}: 受到 {} 点伤害,目前血量 {}".format(monster.name, a, monster.now_hp))


class Monster_big(Monster):
    def __init__(Monster_Boss, name, level):
        super(Monster_big, Monster_Boss).__init__(name, level)
        Monster_Boss.safe = Monster_Boss.max_hp * 0.6
    def damage(Monster_Boss, a):
        if Monster_Boss.safe - a >= 0:
            Monster_Boss.safe = a-Monster_Boss.safe
            print("{}受到 {}点伤害,目前护盾值 {} 目前血量 {}".format(Monster_Boss.name, a, Monster_Boss.safe, Monster_Boss.now_hp))
        else:
            if Monster_Boss.safe > 0:
                Monster_Boss.now_hp -= Monster_Boss.safe
                Monster_Boss.safe = 0
                print("{}受到 {}点伤害,目前护盾值 {} 目前血量 {}".format(Monster_Boss.name, a, Monster_Boss.safe, Monster_Boss.now_hp))
            else:
                Monster_Boss.now_hp -= a
                print("{}受到 {}点伤害,目前护盾值 {} 目前血量 {}".format(Monster_Boss.name, a, Monster_Boss.safe, Monster_Boss.now_hp))


def main():
    playerName=input("请输入角色名：")
    playerRace=input("请输入种族(1、Elf 2、Human)：")
    if playerRace=="1":
        hero=Elf(playerName)
    elif playerRace=="2":
        hero=Human(playerName)
    else:
        print("您输入的种族不存在，请重启程序重新输入")
    
    a = Monster("哥布林", 1)
    b = Monster("牛头怪", 2)
    c = Monster_big("恶魔", 3)
    MonsterNum = [a, b, c]
    r = 1
    while True:
        print("================回合{}================：".format(r))
        MonsterNum[0].damage(hero.attack())
        if MonsterNum[0].now_hp <= 0:
            print("{} 阵亡".format(MonsterNum[0].name))
            hero.up()
            del MonsterNum[0]
        if len(MonsterNum) == 0:
            print("系统：人类赢得胜利!")
            return

        for each in MonsterNum:
            hero.damage(each.attack())
        if hero.now_hp <= 0:
            print("系统：您已失败，请重新开局!")
            return
        r += 1

if __name__ == '__main__':
  main()