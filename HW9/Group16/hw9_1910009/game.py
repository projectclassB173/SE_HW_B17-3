import random
from Hero import Hero
from Monster import Monster, Boss


def main():
    hero = Hero("Asahi", 100, 1, 'human')
    m1 = Monster("Monster1", 60)
    m2 = Monster("Monster2", 60)
    b = Boss("Boss", 80)
    monster_list = [m1, m2, b]
    round = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        while monster_list[0].get_hp() > 0:
            print("*"*20, 'fighting of round {}'.format(round), '*'*20)
            hero.attack(monster_list[0])
            if monster_list[0].get_hp() > 0:
                monster_list[0].attack(hero)
                if hero.get_hp() <= 0:
                    break
            print(hero)
            print(monster_list[0])
            round += 1
        if monster_list[0].get_hp() <= 0:
            del monster_list[0]
            hero.upgrade()

    if hero.get_hp() > 0:
        print('You win,{}'.format(hero.get_name()))
    else:
        print('You lose,{}'.format(hero.get_name()))


if __name__ == '__main__':
    main()
