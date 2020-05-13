import random as k

class Hero:
    #����
    def __init__(hero, name):   #��ʼ����
        hero.name = name     # Ӣ������
        hero.level = 1       # Ӣ�۵ȼ�
        hero.max_hp = hero.level*50  # Ӣ���������
        hero.current_hp = hero.level*50  # Ӣ�۵�ǰ����
    #��������
    def attack(hero):
        atk = k.randint(0, hero.level*10)
        print("==Ӣ�۷��������غ�==")
        return atk
    #��������
    def upgrade(hero):
        hero.current_hp= hero.current_hp+10  #��ǰѪ��
        hero.level = hero.level +1
        print("����Ӣ�۵�ǰ�ȼ� {},��ǰѪ�� {}��{}�ɹ�����".format(hero.name, hero.level, hero.current_hp))

class HeroHuman(Hero):
    def __init__(hero, name):      #���Ⱥ���
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.6        # �������ֵ
    #��������
    def defense(hero, atk):
        is_hurt = k.random()#��������������С��0.4���ܣ�����������
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("���������ܵ� {}���˺�,��ǰѪ�� {}".format(atk, hero.current_hp))
        else:
            print("==�������˹���==")
# �����֧
class HeroSpirit(Hero):
    # ���Ժ���
    def __init__(hero, name):   #��ʼ����
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.8        # �������ֵ

    # ��������
    def defense(hero, atk):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= atk
            print("���������ܵ� {}���˺�,��ǰѪ�� {}".format( atk, hero.current_hp))
        else:
            print("==�������˹���==")

class Monster:
    #����
    def __init__(monster, name, level):     #��ʼ����
        monster.name = name      # ��������
        monster.level = level    # ���޵ȼ�
        monster.max_hp = int(level * 40)  # �����������
        monster.current_hp = int(level * 40)  # ���޵�ǰ����

    # ��������
    def attack(monster):
        atk = k.randint(0, monster.level * 5)
        print("==���޷��������غ�==".format(monster.name))
        return atk

        # ���򷽷�
    def hurt(self, monster):
        self.hp -= monster.damage
        if self.hp > 0:
            print("{2}��ǰ������ɵ��˺�Ϊ{3}��"
                "{0}��Ѫ��Ϊ{3}��"
                "{0}ʣ��Ѫ��Ϊ{1}"
                .format(self.name, self.hp,
                              monster.name, monster.damage))
        else:
         self.hp = 0
         print("{2}��ǰ������ɵ��˺�Ϊ{3}��"
                      "{0}��Ѫ��Ϊ{3}��"
                      "{0}ʣ��Ѫ��Ϊ{1}"
                      .format(self.name, self.hp,
                              monster.name, monster.damage))
        self.death()

        # �����ֶ�
    def defense(monster, atk):
        monster.current_hp -= atk
        print("�����ܵ� {} ���˺�,��ǰѪ�� {}".format( atk, monster.current_hp))

# ����boss����
class bigMonster(Monster):
    # ���Ժ���
    def __init__(self, name, level):
        super(bigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  # ����ֵ
    # ��������
    def defense(self, atk):   # �ܵ��������ȿ۳�����
        if self.shield - atk >= 0:
            self.shield = self.shield
            print("��������boss�ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format( atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("��������boss���ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format( atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("��������boss���ܵ� {}���˺�,��ǰ����ֵ {} Ѫ�� {}".format(self.name, atk, self.shield, self.current_hp))


#����������
def main():
    #����һ��Ӣ�ۣ������͵ȼ����ޣ�һ�������
    hero = HeroHuman("����")
    m1 = Monster("����1��", 1)
    m2 = Monster("����2��", 2)
    m3 = bigMonster("����boss", 3)
    MonsterNum = [m1, m2, m3]
    k = 1
    while True:
        print("==��Ϸ��ʼ==")
        print("��{}�غϣ�".format(k))
        MonsterNum[0].defense(hero.attack())   # Ӣ���ַ���������1,2�͹���Boss
        if MonsterNum[0].current_hp <= 0:   # ����������������б���ɾ��������ޣ�Ӣ������
            print("����{} Ѫ��Ϊ0����".format(MonsterNum[0].name))
            hero.upgrade()
            del MonsterNum[0]
        if len(MonsterNum) == 0:      # Ӣ��ʤ���������ǹ�������Ϊ0
            print("==Ӣ�۳ɹ�������й��ޣ�ȡ��ʤ��==")
            return

        for each in MonsterNum:       # ������������
            hero.defense(each.attack())
        if hero.current_hp <= 0:    # Ӣ������ֵС�ڵ���0��Ϊʧ��
            print("==Ӣ�۹���ʧ�ܣ����������������¿�ʼ��Ϸ==")
            return
        k += 1    # �غ�����1
if __name__ == '__main__':
  main()
  print("==��Ϸ����==")


'''
==��Ϸ��ʼ==
��1�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 1 ���˺�,��ǰѪ�� 39
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
==�������˹���==
==��Ϸ��ʼ==
��2�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 5 ���˺�,��ǰѪ�� 34
==���޷��������غ�==
���������ܵ� 2���˺�,��ǰѪ�� 48
==���޷��������غ�==
���������ܵ� 8���˺�,��ǰѪ�� 40
==���޷��������غ�==
���������ܵ� 1���˺�,��ǰѪ�� 39
==��Ϸ��ʼ==
��3�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 7 ���˺�,��ǰѪ�� 27
==���޷��������غ�==
���������ܵ� 0���˺�,��ǰѪ�� 39
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
==�������˹���==
==��Ϸ��ʼ==
��4�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 8 ���˺�,��ǰѪ�� 19
==���޷��������غ�==
���������ܵ� 3���˺�,��ǰѪ�� 36
==���޷��������غ�==
���������ܵ� 3���˺�,��ǰѪ�� 33
==���޷��������غ�==
==�������˹���==
==��Ϸ��ʼ==
��5�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 7 ���˺�,��ǰѪ�� 12
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
���������ܵ� 6���˺�,��ǰѪ�� 27
==���޷��������غ�==
==�������˹���==
==��Ϸ��ʼ==
��6�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 1 ���˺�,��ǰѪ�� 11
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
���������ܵ� 7���˺�,��ǰѪ�� 20
==���޷��������غ�==
���������ܵ� 6���˺�,��ǰѪ�� 14
==��Ϸ��ʼ==
��7�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 9 ���˺�,��ǰѪ�� 2
==���޷��������غ�==
���������ܵ� 0���˺�,��ǰѪ�� 14
==���޷��������غ�==
==�������˹���==
==���޷��������غ�==
���������ܵ� 2���˺�,��ǰѪ�� 12
==��Ϸ��ʼ==
��8�غϣ�
==Ӣ�۷��������غ�==
�����ܵ� 7 ���˺�,��ǰѪ�� -5
��������1�� Ѫ��Ϊ0����
����Ӣ�۵�ǰ�ȼ� ����,��ǰѪ�� 2��22�ɹ�����
==���޷��������غ�==
���������ܵ� 8���˺�,��ǰѪ�� 14
==���޷��������غ�==
���������ܵ� 15���˺�,��ǰѪ�� -1
==Ӣ�۹���ʧ�ܣ����������������¿�ʼ��Ϸ==
==��Ϸ����==
'''
