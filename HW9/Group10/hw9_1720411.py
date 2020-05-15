import random as r


class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = self.level*20
        self.current_hp = self.level*20

    def attack(self):
        atk = r.randint(0, self.level*10-1)
        print("{}发起了进攻!".format(self.name))
        return atk

    def upgrade(self):
        self.current_hp += 10
        self.level += 1
        print("{}升级，当前血量为{},等级为{}!".format(self.name, self.current_hp, self.level))


class Human(Hero):
    def __init__(self, name):
        super(Human,self).__init__(name)
        self.avd = 0.4

    def defense(self, atk):
        ishurt = r.random()
        if ishurt < self.avd:
            print("Miss!")
        else:
            print("{}受到{}点伤害，当前血量为{}".format(self.name, atk, self.current_hp))


class Spirit(Hero):
    def __init__(self, name):
        super(Spirit, self).__init__(name)
        self.avd = 0.7

    def defense(self,atk):
        ishurt = r.random()
        if ishurt < 0.7:
            print("Miss!")
        else:
            print("{}受到{}点伤害，当前血量为{}".format(self.name, atk, self.current_hp))


class Moster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_hp = int(level * 15)
        self.current_hp = int(level * 15)

    def attack(self):
        atk = r.randint(0, self.level*10-1)
        print("{}发起进攻".format(self.name))
        return atk

    def defense(self,atk):
        self.current_hp -=atk
        print("{}受到{}点伤害，当前血量为{}".format(self.name, atk, self.current_hp))


class Bigmoster(Moster):
    def __init__(self, name, level):
        super(Bigmoster, self).__init__(name, level)
        self.shield = self.max_hp*0.2

    def defense(self,atk):
        if self.shield - atk >= 0:
            self.shield -= atk
            print("{}受到{}点伤害，当前护盾值为{}，血量为{}".format(self.name, atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield -= atk
                print("{}受到{}点伤害，当前护盾值{}血量{}".format(self.name, atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("{}受到{}点伤害，当前护盾值{}血量{}".format(self.name, atk, self.shield, self.current_hp))


def main():
    h = Spirit("妖姬")
    m1 = Moster("哥斯拉", 1)
    m2 = Moster("hyc", 2)
    m3 = Moster("css", 3)
    enemy = [m1, m2, m3]
    round = 1
    while True:
        print("------------round{}------------".format(round))
        enemy[0].defense(h.attack())
        if enemy[0].current_hp <= 0:
            print("{}扑街".format(enemy[0].name))
            h.upgrade()
            del enemy[0]
        if len(enemy) == 0:
            print("{}win".format(h.name))
            break
        for each in enemy:
            h.defense(each.attack())
        if h.current_hp <= 0:
            print("{}lose".format(h.name))
            break
        round += 1


if __name__ == '__main__':
    main()