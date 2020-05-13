import random as r

class Hero:
    def __init__(hero, name):
        hero.name = name
        hero.level = 1
        hero.max_hp = hero.level*60  # 英雄的最大生命值
        hero.n_hp = hero.level*60  # 英雄的目前生命值
    def attack(hero):
        z = r.randint(0, hero.level*20)
        print("{}发动攻击!".format(hero.name))
        return z
    def up(hero):
        hero.n_hp= hero.n_hp+10
        hero.level = hero.level +1
        print("{} 升级,目前等级 {},目前血量 {}".format(hero.name, hero.level, hero.n_hp))

class Human(Hero):
    def __init__(hero, name):
        super(Human, hero).__init__(name)
        hero.avd = 0.5
    def defense(hero, z):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.n_hp -= z
            print("人类：受到 {}点伤害,目前血量 {}".format(z, hero.n_hp))
        else:
            print("人类：miss!")


class Spr(Hero):
    def __init__(hero, name):
        super(Spr, hero).__init__(name)
        hero.avd = 0.8
    def defense(hero, z):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.n_hp -= z
            print("小精灵：受到 {}点伤害,目前血量 {}".format( z, hero.n_hp))
        else:
            print("小精灵：miss!")

class Monster:

    def __init__(monster, name, level):
        monster.name = name
        monster.level = level
        monster.max_hp = int(level * 10)
        monster.n_hp = int(level * 10)
    def attack(monster):
        atk = r.randint(0, monster.level * 10)
        print("{}发动攻击!".format(monster.name))
        return atk
    def defense(monster, z):
        monster.n_hp -= z
        print("{}: 受到 {} 点伤害,目前血量 {}".format(monster.name, z, monster.n_hp))


class Monster_big(Monster):
    def __init__(Monster_Boss, name, level):
        super(Monster_big, Monster_Boss).__init__(name, level)
        Monster_Boss.safe = Monster_Boss.max_hp * 0.4
    def defense(Monster_Boss, z):
        if Monster_Boss.safe - z >= 0:
            Monster_Boss.safe = z-Monster_Boss.safe
            print("{}：受到 {}点伤害,目前护盾值 {} 目前血量 {}".format( Monster_Boss.name,z, Monster_Boss.safe, Monster_Boss.n_hp))
        else:
            if Monster_Boss.safe > 0:
                Monster_Boss.n_hp -= Monster_Boss.safe
                Monster_Boss.safe = 0
                print("{}：受到 {}点伤害,目前护盾值 {} 目前血量 {}".format( Monster_Boss.name,z, Monster_Boss.safe, Monster_Boss.n_hp))
            else:
                Monster_Boss.n_hp -= z
                print("{}：受到 {}点伤害,目前护盾值 {} 目前血量 {}".format(Monster_Boss.name, z, Monster_Boss.safe, Monster_Boss.n_hp))

#主函数
def main():
    playerName=input("请输入角色名：")
    playerRace=input("请输入种族(1、Spr 2、human)：")
    if playerRace=="1":
        hero=Spr(playerName)
    elif playerRace=="2":
        hero=Human(playerName)
    else:
        print("您输入的种族不存在，请重启程序重新输入")
    
    a = Monster("longdd", 1)
    b = Monster("zhou", 2)
    c = Monster_big("yyf", 3)
    MonsterNum = [a, b, c]
    r = 1
    while True:
        print("=======回合{}=======：".format(r))
        MonsterNum[0].defense(hero.attack())
        if MonsterNum[0].n_hp <= 0:
            print("{} 阵亡".format(MonsterNum[0].name))
            hero.up()
            del MonsterNum[0]
        if len(MonsterNum) == 0:
            print("英雄：赢得胜利!")
            return

        for each in MonsterNum:
            hero.defense(each.attack())
        if hero.n_hp <= 0:    # 失败条件：英雄当前的血条为0
            print("英雄：您已失败，请重新开局!")
            return
        r += 1

if __name__ == '__main__':
  main()

