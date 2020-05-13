# �����������ϰ
# ��дһ������޵�С��Ϸ��
# ��ϷҪ�����£� 
# 1. ��Ϸ�н�ɫ��Ӣ�ۺ͹������ִ����͡�
# 2. ��Ϸ��Ӣ�ۺ͹����������͹�����֪����һ��������
# 3. Ӣ�۾������֡�����(��3��������ǰ��������ǰ�ȼ���������������������Ե����ԣ����й����ͷ���������
#    ����ʱ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ���������������������ܵ��ε����Ĺ����� 
#    ���缶��Ϊ1ʱ��[0,10)��Χ���������һ������Ϊ������������Ϊ2����[0,20)��Χ�ڲ���һ������Ϊ��������
#    Ӣ�۾���������ѡ���壬����;��顣 �������������Եĸߵ͡�
#    �ܵ�����ʱ����������ԣ����Զ�ܵ��Է��Ĺ����� ���磺��ǰӢ�������Ϊ0.4�� ���ܵ��Է�m�㹥��ʱ����
#    ��һ����0��1��֮������������������С�������0.4�����ܵ��˴ι������ܵ��˺��������ܵ�m���˺���
# 4. ����Ҳ�������֡�����(��3��������ǰ��������ǰ�ȼ�������������ԡ� ���й����ͷ���������
#    ���޼���3������1����2��ֻ�м�������Ĺ��������졣 ������Ϊ����ޡ�
#    ���й��޵Ĺ���������Ӣ�۵Ĺ�������ԭ����ͬ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ����������
#    �����������ܵ��ε����Ĺ����� 
#    ����޾���һ������Ķ������ԡ��յ�������ʱ�����ȼ��ٶ��Ƶķ��������Ʒ�������Ϊ0 ���Ժ�ż���������
# 5. ��дһ���ܵ���ڳ�������һ��Ӣ�ۣ� �����͵ȼ����ޣ�һ������ޣ� �趨ѭ��������Ӣ�ۺ͹��ް�˳���������͹�����
#    ֱ��Ӣ�����������й��ޱ�ɱ����
# 6. ��Ϸ��������ÿ�غϹ�����������Ӧ��ӡ����ܵ����˺����Լ���ǰ����������Ϸ����ӡӢ����Win����Lose��

import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name    # ����
        self.max = hp       # Ѫ��
        self._hp = hp       # Ѫ��
        self.level = level  # �ȼ�

    def get_name(self):
        return self.name
    def get_hp(self):
        return self._hp
    def get_level(self):
        return self.level
    def attack(self, target):
        raise NotImplementedError
    def __str__(self):
        return '{}��{}����\t ʣ��Ѫ����{} \t '.format(self.name, self.level, self._hp)

class Hero(Person):
    def __init__(self, name, hp, level, race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':   # ����
            self.agile = 0.4
        elif self.race == 'elves':   # ����
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
            print('���ܵ���{}���˺�'.format(hurt))
        else:
            print('��ɹ�����˹���!')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 20
        self._hp = self.max
        print('-'*10, '��ϲ�㣡����������{}����Ѫ����������Ϊ{}'.format(self.level,self.max))


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
        print('{}�ܵ���{}���˺�'.format(self.name, hurt))

def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 80   # ����

    def attack(self, hero):
        hurt = random.randint(30, 40)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
            print("{}�ܵ�{}���˺�".format(self.name, hurt))


def main():
    hero = Hero("������", 100, 1, 'human')
    monster1 = Monster("��������", 30, 1)
    monster2 = Monster("��ѩ����", 60, 2)
    boss = Boss("�ʼҾ���", 100)
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
        print('��ϲ�㣬ʤ���ˣ�{}'.format(hero.get_name()))
    else:
        print('�ܿ�ϧ�������ˡ����´�����')

if __name__ == '__main__':
    main()

# D:\1720419\xiangmushizhan\�����\venv\Scripts\python.exe D:/1720419/xiangmushizhan/�����/dgs
# ******************** round 1 ********************
# ���������ܵ���2���˺�
# ���ܵ���4���˺�
# �����У�1����	 ʣ��Ѫ����96
# ����������1����	 ʣ��Ѫ����28
# ******************** round 2 ********************
# ���������ܵ���4���˺�
# ��ɹ�����˹���!
# �����У�1����	 ʣ��Ѫ����96
# ����������1����	 ʣ��Ѫ����24
# ******************** round 3 ********************
# ���������ܵ���9���˺�
# ���ܵ���2���˺�
# �����У�1����	 ʣ��Ѫ����94
# ����������1����	 ʣ��Ѫ����15
# ******************** round 4 ********************
# ���������ܵ���9���˺�
# ���ܵ���3���˺�
# �����У�1����	 ʣ��Ѫ����91
# ����������1����	 ʣ��Ѫ����6
# ******************** round 5 ********************
# ���������ܵ���9���˺�
# �����У�1����	 ʣ��Ѫ����91
# ����������1����	 ʣ��Ѫ����-3
# ---------- ��ϲ�㣡����������2����Ѫ����������Ϊ120
# ******************** round 6 ********************
# ��ѩ�����ܵ���17���˺�
# ��ɹ�����˹���!
# �����У�2����	 ʣ��Ѫ����120
# ��ѩ���飨2����	 ʣ��Ѫ����43
# ******************** round 7 ********************
# ��ѩ�����ܵ���10���˺�
# ��ɹ�����˹���!
# �����У�2����	 ʣ��Ѫ����120
# ��ѩ���飨2����	 ʣ��Ѫ����33
# ******************** round 8 ********************
# ��ѩ�����ܵ���14���˺�
# ���ܵ���11���˺�
# �����У�2����	 ʣ��Ѫ����109
# ��ѩ���飨2����	 ʣ��Ѫ����19
# ******************** round 9 ********************
# ��ѩ�����ܵ���20���˺�
# �����У�2����	 ʣ��Ѫ����109
# ��ѩ���飨2����	 ʣ��Ѫ����-1
# ---------- ��ϲ�㣡����������3����Ѫ����������Ϊ140
# ******************** round 10 ********************
# ��ɹ�����˹���!
# �����У�3����	 ʣ��Ѫ����140
# �ʼҾ��ˣ�3����	 ʣ��Ѫ����100
# ******************** round 11 ********************
# ��ɹ�����˹���!
# �����У�3����	 ʣ��Ѫ����140
# �ʼҾ��ˣ�3����	 ʣ��Ѫ����100
# ******************** round 12 ********************
# ���ܵ���40���˺�
# �����У�3����	 ʣ��Ѫ����100
# �ʼҾ��ˣ�3����	 ʣ��Ѫ����100
# ******************** round 13 ********************
# �ʼҾ����ܵ�24���˺�
# ���ܵ���30���˺�
# �����У�3����	 ʣ��Ѫ����70
# �ʼҾ��ˣ�3����	 ʣ��Ѫ����76
# ******************** round 14 ********************
# �ʼҾ����ܵ�24���˺�
# ���ܵ���35���˺�
# �����У�3����	 ʣ��Ѫ����35
# �ʼҾ��ˣ�3����	 ʣ��Ѫ����52
# ******************** round 15 ********************
# �ʼҾ����ܵ�28���˺�
# ���ܵ���38���˺�
# �ܿ�ϧ�������ˡ����´�����
