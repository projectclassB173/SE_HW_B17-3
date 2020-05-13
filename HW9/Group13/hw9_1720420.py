##�����������ϰ
##��дһ������޵�С��Ϸ��
##��ϷҪ�����£�
##1. ��Ϸ�н�ɫ��Ӣ�ۺ͹������ִ����͡�
##2. ��Ϸ��Ӣ�ۺ͹����������͹�����֪����һ��������
##3. Ӣ�۾������֡�����(��3��������ǰ��������ǰ�ȼ���������������������Ե����ԣ����й����ͷ���������
##����ʱ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ���������������������ܵ��ε����Ĺ�����
##���缶��Ϊ1ʱ��[0,10)��Χ���������һ������Ϊ������������Ϊ2����[0,20)��Χ�ڲ���һ������Ϊ��������
##Ӣ�۾���������ѡ���壬����;��顣 �������������Եĸߵ͡�
##�ܵ�����ʱ����������ԣ����Զ�ܵ��Է��Ĺ����� ���磺��ǰӢ�������Ϊ0.4�� ���ܵ��Է�m�㹥��ʱ����
##��һ����0��1��֮������������������С�������0.4�����ܵ��˴ι������ܵ��˺��������ܵ�m���˺���
##4. ����Ҳ�������֡�����(��3��������ǰ��������ǰ�ȼ�������������ԡ� ���й����ͷ���������
##���޼���3������1����2��ֻ�м�������Ĺ��������졣 ������Ϊ����ޡ�
##���й��޵Ĺ���������Ӣ�۵Ĺ�������ԭ����ͬ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ����������
##�����������ܵ��ε����Ĺ�����
##����޾���һ������Ķ������ԡ��յ�������ʱ�����ȼ��ٶ��Ƶķ��������Ʒ�������Ϊ0 ���Ժ�ż���������
##5. ��дһ���ܵ���ڳ�������һ��Ӣ�ۣ� �����͵ȼ����ޣ�һ������ޣ� �趨ѭ��������Ӣ�ۺ͹��ް�˳���������͹�����
##ֱ��Ӣ�����������й��ޱ�ɱ����
##6. ��Ϸ��������ÿ�غϹ�����������Ӧ��ӡ����ܵ����˺����Լ���ǰ����������Ϸ����ӡӢ����Win����Lose��


import random as ra


class Person(object):
    def __init__(self, name, HP, level):
        self.name = name
        self.max = HP
        self._hp = HP
        self.level = level

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

class Monster(Person):
    def __init__(self, name, HP=20, level=1):
        super().__init__(name, HP, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = ra.randint(0, 10)
        if self.level == 2:
            hurt = ra.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('{}�ܵ���{}���˺�'.format(self.name, hurt))


class Boss(Person):
    def __init__(self, name, HP):
        super().__init__(name, HP, 4)
        self.shield = 30

    def attack(self, hero):
        hurt = ra.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print("{}�ܵ�{}���˺�,����ʣ��{}".format(self.name, hurt, self.shield))
        else:
            if self.shield > 0:
                self._hp -= self.shield
                self.shield = 0
                print("{}�ܵ�{}���˺�,����ʣ��{}".format(self.name, hurt, self.shield))
            else:
                self._hp -= hurt
                print("{}�ܵ�{}���˺�,����ʣ��{}".format(self.name, hurt, self.shield))


class Hero(Person):
    def __init__(self, name, HP=30, level=1, race='����'):
        super().__init__(name, HP, level)
        self.race = race
        if self.race == '����':
            self.agile = 0.4
        elif self.race == '����':
            self.agile = 0.8

    def attack(self, monster):
        if self.level == 1:
            hurt = ra.randint(0, 15)
        elif self.level == 2:
            hurt = ra.randint(15,20)
        elif self.level == 3:
            hurt = ra.randint(30,50)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = ra.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('���ܵ���{}���˺�'.format(hurt))
        else:
            print('Miss! ����˹���')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-'*10, '��������{}��,Ѫ������Ϊ{}'.format(self.level, self._hp), '-'*10)


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


def main():
    hero = Hero("������", 100, 1, '����')
    m1 = Monster("С��1��")
    m2 = Monster("С��2��", 80, 2)
    boss = Boss("������", 100)
    monster_list = [m1, m2, boss]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*20, '��{}�غ�'.format(r), '*'*20)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_hp() > 0:
        print('��ʤ���ˣ���{}'.format(hero.get_name()))
    else:
        print('������...')


if __name__ == '__main__':
    main()

C:\Users\hasee\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/hasee/PycharmProjects/untitled/FPgrowth/GAME.py
******************** ��1�غ� ********************
С��1���ܵ���15���˺�
Miss! �����˹���
Name:������	 HP: 100 	 Level:1
Name:С��1��	 HP: 5 	 Level:1
******************** ��2�غ� ********************
С��1���ܵ���9���˺�
Name:������	 HP: 100 	 Level:1
Name:С��1��	 HP: -4 	 Level:1
---------- ��������2��,Ѫ������Ϊ110 ----------
******************** ��3�غ� ********************
С��2���ܵ���15���˺�
���ܵ���14���˺�
Name:������	 HP: 96 	 Level:2
Name:С��2��	 HP: 65 	 Level:2
******************** ��4�غ� ********************
С��2���ܵ���15���˺�
Miss! �����˹���
Name:������	 HP: 96 	 Level:2
Name:С��2��	 HP: 50 	 Level:2
******************** ��5�غ� ********************
С��2���ܵ���17���˺�
Miss! �����˹���
Name:������	 HP: 96 	 Level:2
Name:С��2��	 HP: 33 	 Level:2
******************** ��6�غ� ********************
С��2���ܵ���16���˺�
Miss! �����˹���
Name:������	 HP: 96 	 Level:2
Name:С��2��	 HP: 17 	 Level:2
******************** ��7�غ� ********************
С��2���ܵ���18���˺�
Name:������	 HP: 96 	 Level:2
Name:С��2��	 HP: -1 	 Level:2
---------- ��������3��,Ѫ������Ϊ120 ----------
******************** ��8�غ� ********************
�������ܵ�31���˺�,��ǰ����ʣ��0
���ܵ���21���˺�
Name:������	 HP: 99 	 Level:3
Name:������	 HP: 70 	 Level:4
******************** ��9�غ� ********************
�������ܵ�48���˺�,��ǰ����ʣ��0
Miss! �����˹���
Name:������	 HP: 99 	 Level:3
Name:������	 HP: 22 	 Level:4
******************** ��10�غ� ********************
�������ܵ�45���˺�,��ǰ����ʣ��0
Name:������	 HP: 99 	 Level:3
Name:������	 HP: -23 	 Level:4
---------- ��������4��,Ѫ������Ϊ130 ----------
��ʤ���ˣ���������

�����ѽ������˳����� 0
