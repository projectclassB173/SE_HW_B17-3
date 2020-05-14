import random  #随机数

class ZWH(object):
    #  游戏中角色有英雄和怪兽两种大类型。
    #  游戏中英雄和怪兽轮流发送攻击，直到有一方死亡。
    def __init__(self, name, hp, level):
        self.name = name   #名字
        self.max_hp = hp    # 当前生命
        self.now_hp = hp    # 级别
        self.level = level      #当前等级的最大生命属性。
    def get_name(self):
        return self.name     #名字
    def getnow_hp(self):
        return self.now_hp     #当前生命
    def get_level(self):
        return self.level     # 级别
    def attack(self, target):
        raise NotImplementedError    #目标
    def __str__(self):
        return '{}的生命值还剩{}滴血！但是等级达到了{}级！'.format(self.name, self.now_hp, self.level)

class Hero(ZWH):
    #    英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
    #    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
    #    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
    #    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
    #    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
    #    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
    def __init__(self, name, hp=40, level=1, race='elf'):
        # 先设置种族为人类，继承英雄的基础属性，
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.5
        elif self.race == 'elf':
            self.agile = 0.7
        # 不同种族有不同的灵活性，人类为0.4，精灵0.6

    def attack(self, monster): # 伤害判定
        if self.level == 1:
            hurt = random.randint(0, 10)
            # 等级1伤害在[0,10)范围内产生一个随机数作为攻击力
        elif self.level == 2:
            hurt = random.randint(0, 20)
            # 等级2伤害在[0,20)范围内产生一个随机数作为攻击力
        elif self.level == 3:
            hurt = random.randint(0, 30)
            #等级3伤害在[0, 30)范围内产生一个随机数作为攻击力
        monster.defence(hurt)

    def defence(self, hurt):   # 承伤判定
        luck = random.random()
        if luck >= self.agile:
            self.now_hp -= hurt
            print('被打中了！ 你承受了{}点伤害'.format(hurt))
        else:
            print('好险啊！只差了一点就要受伤了！')

    def upgrade(self):    # 升级判定
        self.level += 1
        self.max_hp = self.max_hp + 10  # 每升级 血量加10
        self.now_hp = self.max_hp
        print('='*10, '你升级到{}级'.format(self.level), '='*10)

class Monster(ZWH):
    #    怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
    #    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
    #    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
    #    被攻击对象即受到次点数的攻击。
    def __init__(self, name, hp=30, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):  # 伤害判定
        print("现在是{}是你的对手 !".format(self.name))
        if self.level == 1:
            hurt = random.randint(0, 10)
            # 第一个怪兽   在[0,10)范围内产生一个随机数作为攻击力
        if self.level == 2:
            hurt = random.randint(0, 20)
           # 第二个怪兽   在[0,10)范围内产生一个随机数作为攻击力
        hero.defence(hurt)


    def defence(self, hurt):
        self.now_hp -= hurt
        print('小兵受到了{}点伤害'.format(self.level,hurt))

class Boss(ZWH):
    #    与普通怪兽基本相同。
    #    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        # 大怪兽属性相同
        self.shield = 60
        # 大怪兽有护盾  护盾为60

    def attack(self, hero):
        hurt = random.randint(0, 30)
        # 大怪兽进行攻击 伤害在[0,30)范围内产生一个随机数作为攻击力
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        # 优先护盾
        if self.shield <= 0:
            self.now_hp -= hurt
        # 超过护盾受伤
        print("{}受到了{}点伤害".format(self.name,hurt))

def main():
    playerRace = input("你的英雄名字叫周杰伦 请输入他的种族(a代表人族 b代表精灵)：")
    #  英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
    if playerRace == "a":
        cc = 'elf'
    elif playerRace == "b":
        cc = 'human'

    # 生成英雄和怪兽实例
    hero = Hero("周杰伦", 100, 1, cc)
    monster1 = Monster("小兵1")
    monster2 = Monster("小兵2")
    boss = Boss("终极大boss", 100)
    # 大怪兽
    monster_list = [monster1,  monster2, boss]
    r = 1
    while hero.getnow_hp() > 0 and len(monster_list) > 0:
        #   编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
        #   直到英雄死亡或所有怪兽被杀死。
        #   游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose
        monster = n_m(monster_list)
        while monster.getnow_hp() > 0:                 #发起攻击
            print('-'*10, '第{}回合'.format(r), '-'*10)
            hero.attack(monster)
            if monster.getnow_hp() > 0:                #怪物没死，英雄被打
                monster.attack(hero)
                if hero.getnow_hp() <= 0:              #英雄没死，怪物被打
                    break
            print(hero)
            print(monster)
            r += 1
        if monster.getnow_hp() <= 0:                    #无怪物就胜利
            monster_list.remove(monster)
            hero.upgrade()
            monster = n_m(monster_list)

    if hero.getnow_hp() > 0:                            #输出胜利还是失败
        print('{}胜利！'.format(hero.get_name()))
    else:
        print("你失败了！下次继续加油吧")

def n_m(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]
#    编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
if __name__ == '__main__':
    main()


'''
你的英雄名字叫周杰伦 请输入他的种族(a代表人族 b代表精灵)：a
---------- 第1回合 ----------
小兵受到了1点伤害
现在是小兵1是你的对手 !
被打中了！ 你承受了2点伤害
周杰伦的生命值还剩98滴血！但是等级达到了1级！
小兵1的生命值还剩23滴血！但是等级达到了1级！
---------- 第2回合 ----------
小兵受到了1点伤害
现在是小兵1是你的对手 !
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩98滴血！但是等级达到了1级！
小兵1的生命值还剩13滴血！但是等级达到了1级！
---------- 第3回合 ----------
小兵受到了1点伤害
现在是小兵1是你的对手 !
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩98滴血！但是等级达到了1级！
小兵1的生命值还剩9滴血！但是等级达到了1级！
---------- 第4回合 ----------
小兵受到了1点伤害
现在是小兵1是你的对手 !
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩98滴血！但是等级达到了1级！
小兵1的生命值还剩3滴血！但是等级达到了1级！
---------- 第5回合 ----------
小兵受到了1点伤害
周杰伦的生命值还剩98滴血！但是等级达到了1级！
小兵1的生命值还剩-5滴血！但是等级达到了1级！
========== 你升级到2级 ==========
---------- 第6回合 ----------
小兵受到了1点伤害
现在是小兵2是你的对手 !
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩110滴血！但是等级达到了2级！
小兵2的生命值还剩30滴血！但是等级达到了1级！
---------- 第7回合 ----------
小兵受到了1点伤害
现在是小兵2是你的对手 !
被打中了！ 你承受了5点伤害
周杰伦的生命值还剩105滴血！但是等级达到了2级！
小兵2的生命值还剩23滴血！但是等级达到了1级！
---------- 第8回合 ----------
小兵受到了1点伤害
现在是小兵2是你的对手 !
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩105滴血！但是等级达到了2级！
小兵2的生命值还剩4滴血！但是等级达到了1级！
---------- 第9回合 ----------
小兵受到了1点伤害
周杰伦的生命值还剩105滴血！但是等级达到了2级！
小兵2的生命值还剩-7滴血！但是等级达到了1级！
========== 你升级到3级 ==========
---------- 第10回合 ----------
终极大boss受到了22点伤害
被打中了！ 你承受了30点伤害
周杰伦的生命值还剩90滴血！但是等级达到了3级！
终极大boss的生命值还剩100滴血！但是等级达到了3级！
---------- 第11回合 ----------
终极大boss受到了16点伤害
被打中了！ 你承受了2点伤害
周杰伦的生命值还剩88滴血！但是等级达到了3级！
终极大boss的生命值还剩100滴血！但是等级达到了3级！
---------- 第12回合 ----------
终极大boss受到了14点伤害
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩88滴血！但是等级达到了3级！
终极大boss的生命值还剩100滴血！但是等级达到了3级！
---------- 第13回合 ----------
终极大boss受到了25点伤害
被打中了！ 你承受了1点伤害
周杰伦的生命值还剩87滴血！但是等级达到了3级！
终极大boss的生命值还剩75滴血！但是等级达到了3级！
---------- 第14回合 ----------
终极大boss受到了19点伤害
被打中了！ 你承受了9点伤害
周杰伦的生命值还剩78滴血！但是等级达到了3级！
终极大boss的生命值还剩56滴血！但是等级达到了3级！
---------- 第15回合 ----------
终极大boss受到了26点伤害
被打中了！ 你承受了19点伤害
周杰伦的生命值还剩59滴血！但是等级达到了3级！
终极大boss的生命值还剩30滴血！但是等级达到了3级！
---------- 第16回合 ----------
终极大boss受到了22点伤害
被打中了！ 你承受了25点伤害
周杰伦的生命值还剩34滴血！但是等级达到了3级！
终极大boss的生命值还剩8滴血！但是等级达到了3级！
---------- 第17回合 ----------
终极大boss受到了3点伤害
好险啊！只差了一点就要受伤了！
周杰伦的生命值还剩34滴血！但是等级达到了3级！
终极大boss的生命值还剩5滴血！但是等级达到了3级！
---------- 第18回合 ----------
终极大boss受到了20点伤害
周杰伦的生命值还剩34滴血！但是等级达到了3级！
终极大boss的生命值还剩-15滴血！但是等级达到了3级！
========== 你升级到4级 ==========
周杰伦胜利！
'''