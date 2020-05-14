import random
class Person(object):
    def __init__(self,name,hp,level):
        self.name = name #����
        self.max = hp #Ѫ��
        self._hp = hp #Ѫ��
        self.level = level #�ȼ�

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

class Hero(Person):
    def __init__(self, name,hp=30,level=1,race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human': #Ӣ��
            self.agile = 0.4
        elif self.race == 'elves': #����
            self.agile = 0.8
    def attack(self,monster):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(5,20)
        elif self.level==3:
            hurt=random.randint(5,30)
        monster.defence(hurt)
    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('���У����ܵ�{}���˺�'.format(hurt))
        else:
            print('��������û���ܵ�������')
    def upgrade(self):
        self.level += 1
        self.max = self.max + 20
        self._hp = self.max
        print('-' * 10, '��ɹ�������{}����Ѫ������Ϊ{}'.format(self.level, self._hp), '-'*10)

class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)
    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)
        hero.defence(hurt)
    def defence(self, hurt):
        self._hp -= hurt
        print('���У�{}�ܵ���{}���˺�'.format(self.name, hurt))
def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]

class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 4)
        self.shield = 300   # ����
    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)
    def defence(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print("{}�ܵ�{}���˺�,��ǰ����ʣ��{}".format(self.name,hurt,self.shield))
        else:
            if self.shield > 0:
                self._hp -= self.shield
                self.shield = 0
                print("{}�ܵ�{}���˺�,��ǰ����ʣ��{}".format(self.name,hurt,self.shield))
            else:
                self._hp -= hurt
                print("{}�ܵ�{}���˺�,��ǰ����ʣ��{}".format(self.name,hurt,self.shield))

def main():
    hero1 = Hero("Ӣ��", 200, 1, 'human')
    mon1 = Monster("С��1��")
    mon2 = Monster("С��2��", 80, 2)
    boss = Boss("��BOSS", 100)
    monster_list = [mon1, mon2, boss]
    r = 1
    while hero1.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*20,'round {}'.format(r),'*'*20)
            hero1.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero1)
                if hero1.get_hp() <= 0:
                    break
            print(hero1)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero1.upgrade()
    if hero1.get_hp() > 0:
        print('{}��ͨ����'.format(hero1.get_name()))
    else:
        print('{}������!��������ս�ɣ�'.format(hero1.get_name()))

if __name__ == '__main__':
    main()


#******************** round 1 ********************
# ���У�С��1���ܵ���10���˺�
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 200 	 Level:1
# Name:С��1��	 HP: 10 	 Level:1
# ******************** round 2 ********************
# ���У�С��1���ܵ���7���˺�
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 200 	 Level:1
# Name:С��1��	 HP: 3 	 Level:1
# ******************** round 3 ********************
# ���У�С��1���ܵ���5���˺�
# Name:Ӣ��	 HP: 200 	 Level:1
# Name:С��1��	 HP: -2 	 Level:1
# ---------- ��ɹ�������2����Ѫ������Ϊ220 ----------
# ******************** round 4 ********************
# ���У�С��2���ܵ���20���˺�
# ���У����ܵ�5���˺�
# Name:Ӣ��	 HP: 215 	 Level:2
# Name:С��2��	 HP: 60 	 Level:2
# ******************** round 5 ********************
# ���У�С��2���ܵ���16���˺�
# ���У����ܵ�10���˺�
# Name:Ӣ��	 HP: 205 	 Level:2
# Name:С��2��	 HP: 44 	 Level:2
# ******************** round 6 ********************
# ���У�С��2���ܵ���11���˺�
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 205 	 Level:2
# Name:С��2��	 HP: 33 	 Level:2
# ******************** round 7 ********************
# ���У�С��2���ܵ���14���˺�
# ���У����ܵ�14���˺�
# Name:Ӣ��	 HP: 191 	 Level:2
# Name:С��2��	 HP: 19 	 Level:2
# ******************** round 8 ********************
# ���У�С��2���ܵ���8���˺�
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 191 	 Level:2
# Name:С��2��	 HP: 11 	 Level:2
# ******************** round 9 ********************
# ���У�С��2���ܵ���6���˺�
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 191 	 Level:2
# Name:С��2��	 HP: 5 	 Level:2
# ******************** round 10 ********************
# ���У�С��2���ܵ���5���˺�
# Name:Ӣ��	 HP: 191 	 Level:2
# Name:С��2��	 HP: 0 	 Level:2
# ---------- ��ɹ�������3����Ѫ������Ϊ240 ----------
# ******************** round 11 ********************
# ��BOSS�ܵ�29���˺�,��ǰ����ʣ��271
# ���У����ܵ�12���˺�
# Name:Ӣ��	 HP: 228 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 12 ********************
# ��BOSS�ܵ�11���˺�,��ǰ����ʣ��260
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 228 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 13 ********************
# ��BOSS�ܵ�16���˺�,��ǰ����ʣ��244
# ���У����ܵ�28���˺�
# Name:Ӣ��	 HP: 200 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 14 ********************
# ��BOSS�ܵ�26���˺�,��ǰ����ʣ��218
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 200 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 15 ********************
# ��BOSS�ܵ�29���˺�,��ǰ����ʣ��189
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 200 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 16 ********************
# ��BOSS�ܵ�12���˺�,��ǰ����ʣ��177
# ���У����ܵ�12���˺�
# Name:Ӣ��	 HP: 188 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 17 ********************
# ��BOSS�ܵ�24���˺�,��ǰ����ʣ��153
# ���У����ܵ�6���˺�
# Name:Ӣ��	 HP: 182 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 18 ********************
# ��BOSS�ܵ�12���˺�,��ǰ����ʣ��141
# ���У����ܵ�21���˺�
# Name:Ӣ��	 HP: 161 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 19 ********************
# ��BOSS�ܵ�22���˺�,��ǰ����ʣ��119
# ���У����ܵ�8���˺�
# Name:Ӣ��	 HP: 153 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 20 ********************
# ��BOSS�ܵ�19���˺�,��ǰ����ʣ��100
# ���У����ܵ�30���˺�
# Name:Ӣ��	 HP: 123 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 21 ********************
# ��BOSS�ܵ�8���˺�,��ǰ����ʣ��92
# ���У����ܵ�23���˺�
# Name:Ӣ��	 HP: 100 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 22 ********************
# ��BOSS�ܵ�6���˺�,��ǰ����ʣ��86
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 100 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 23 ********************
# ��BOSS�ܵ�24���˺�,��ǰ����ʣ��62
# ���У����ܵ�1���˺�
# Name:Ӣ��	 HP: 99 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 24 ********************
# ��BOSS�ܵ�16���˺�,��ǰ����ʣ��46
# ���У����ܵ�1���˺�
# Name:Ӣ��	 HP: 98 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 25 ********************
# ��BOSS�ܵ�25���˺�,��ǰ����ʣ��21
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 98 	 Level:3
# Name:��BOSS	 HP: 100 	 Level:4
# ******************** round 26 ********************
# ��BOSS�ܵ�24���˺�,��ǰ����ʣ��0
# ���У����ܵ�1���˺�
# Name:Ӣ��	 HP: 97 	 Level:3
# Name:��BOSS	 HP: 79 	 Level:4
# ******************** round 27 ********************
# ��BOSS�ܵ�5���˺�,��ǰ����ʣ��0
# ���У����ܵ�10���˺�
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: 74 	 Level:4
# ******************** round 28 ********************
# ��BOSS�ܵ�11���˺�,��ǰ����ʣ��0
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: 63 	 Level:4
# ******************** round 29 ********************
# ��BOSS�ܵ�7���˺�,��ǰ����ʣ��0
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: 56 	 Level:4
# ******************** round 30 ********************
# ��BOSS�ܵ�30���˺�,��ǰ����ʣ��0
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: 26 	 Level:4
# ******************** round 31 ********************
# ��BOSS�ܵ�25���˺�,��ǰ����ʣ��0
# ��������û���ܵ�������
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: 1 	 Level:4
# ******************** round 32 ********************
# ��BOSS�ܵ�17���˺�,��ǰ����ʣ��0
# Name:Ӣ��	 HP: 87 	 Level:3
# Name:��BOSS	 HP: -16 	 Level:4
# ---------- ��ɹ�������4����Ѫ������Ϊ260 ----------
# Ӣ����ͨ����
