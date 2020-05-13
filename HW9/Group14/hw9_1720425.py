import random


class Heroes:
    def __init__(self, name, level, max_health, race, agility):
        self.name = name

        if int(level) < 1:
            self.level = 1
        else:
            self.level = int(level)

        self.health = max_health
        self.max_health = max_health
        self.race = race

        if agility < 0:
            self.agility = 0

        elif agility > 1:
            self.agility = 1

        else:
            self.agility = agility

    def attack(self):
        damage = random.randint(0, self.level * 10 - 1)
        print("{", self.name, "}发起了 ", damage, " 点攻击", sep="")
        return damage

    def defense(self, hurt):
        if self.agility > random.randint(0, 10) / 10:
            print("{", self.name, "}受到了 0 点伤害，当前血量为 ", self.health, sep="")
        else:
            self.health -= hurt
            print("{", self.name, "}受到了 ", hurt, " 点伤害，当前血量为 ", self.health, sep="")


class Monsters:
    def __init__(self, name, level, race):
        self.name = name

        if int(level) < 1:
            self.level = 1
        else:
            self.level = int(level)

        self.health = self.level * 100
        self.max_health = self.level * 100

        if int(level) >= 3:
            self.armor = 100
        else:
            self.armor = 0

        self.race = race

    def attack(self):
        damage = random.randint(0, self.level * 10 - 1)
        print("{", self.name, "}发起了 ", damage, " 点攻击", sep="")
        return damage

    def defense(self, hurt):
        if hurt >= 0:
            if self.armor <= 0:
                self.health -= hurt
                print("{", self.name, "}受到了 ", hurt, " 点伤害，当前血量为 ", self.health, sep="")

            elif self.armor >= hurt:
                self.armor -= hurt
                print("{", self.name, "}受到了 ", hurt, " 点伤害，当前血量为 ", self.health, " ，当前护甲为 ", self.armor, sep="")

            else:
                self.armor -= hurt
                self.health = self.health + self.armor
                print("{", self.name, "}受到了 ", hurt, " 点伤害，当前血量为 ", self.health, sep="")

        else:
            print("{", self.name, "}受到了 0 点伤害，当前血量为 ", self.health, sep="")


def main():
    player1 = Heroes("枪手", 1, 150, "Dwarfs", 0.3)
    player2 = Heroes("工程兵", 1, 125, "Dwarfs", 0.2)
    player3 = Heroes("钻机手", 1, 150, "Dwarfs", 0.5)
    player4 = Heroes("侦察兵", 1, 100, "Dwarfs", 0.8)
    monster1 = Monsters("战士异虫", 1, "Bugs")
    monster2 = Monsters("刀锋异虫", 2, "Bugs")
    monster3 = Monsters("大自爆虫", 3, "Bugs")

    players = [player1, player2, player3, player4]
    monsters = [monster1, monster2, monster3]
    rounds = 0

    while len(monsters) > 0 and len(players) > 0:
        rounds += 1
        print("第 ", rounds, " 回合 ---------------------------------------------", sep="")

        monsters[0].defense(players[0].attack())
        if monsters[0].health <= 0:
            print("{", monsters[0].name, "}死亡了！", sep="")
            monsters.pop(0)
            if len(monsters) == 0:
                break

            if players[0].level < 3:
                players[0].level += 1
                players[0].health = players[0].max_health
                print("{", players[0].name, "}升级，当前等级为 ", players[0].level, " ，当前血量为 ", players[0].health, sep="")
            else:
                players[0].health = players[0].max_health
                print("{", players[0].name, "}已达满级，当前血量为 ", players[0].health, sep="")

        players[0].defense(monsters[0].attack())
        if players[0].health <= 0:
            print("{", players[0].name, "}倒地了！", sep="")
            players.pop(0)
            if len(players) == 0:
                break

        print("")

    print("")
    if len(players) == 0:
        print("Lose！")

    if len(monsters) == 0:
        print("Win！")


if __name__ == '__main__':
    main()
