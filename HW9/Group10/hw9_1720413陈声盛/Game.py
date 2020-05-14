# 面向对象编程练习
# 编写一个打怪兽的小游戏。
# 游戏要求如下：
# 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
#    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#    被攻击对象即受到次点数的攻击。
#    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

from  Monster import  Monster,Boss
from  Hero import  Hero
def main():
    name = input("请输入英雄姓名：")
    race = input("请输入英雄种族：\n1.人族 2.精灵族\n")
    hero = Hero(name,100,1,race)
    montser1=Monster('咸鱼')
    montser2=Monster('牛头人',80,1)
    boss=Boss('魔王',100)
    montser_list =[montser1,montser2,boss]
    num_mon = 1
    print("-" * 50)
    print("战斗开始")
    while hero.get_hp()>0 and len(montser_list) >0:
        monster = next_monster(montser_list)
        print("-" * 50)
        print("遇到第%d只怪兽" %num_mon)

        round = 1
        while monster.get_hp() >0:
            print('*'*20,'round {}'.format(round),'*'*20)
            hero.attack(monster)
            if monster.get_hp()>0:
                monster.attack(hero)
                if hero.get_hp()<=0:
                    break
            print(hero)
            print(monster)
            round+=1
        if hero.get_hp()>0 and monster.get_hp()<=0:
            print("-" * 50)
            print('{}获得了胜利，获得了大量经验值'.format(hero.get_name()))
            montser_list.remove(monster)
            hero.upgrade()
            monster = next_monster(montser_list)
            num_mon += 1
        elif hero.get_hp()<=0 and monster.get_hp()<=0:
            print("同归于尽！")
            break
        elif hero.get_hp()<=0 and monster.get_hp()>=0:
            print('战败，真的菜！')
            break
    if (len(montser_list) == 0):
        print("恭喜{}通关了游戏".format(hero.get_name()))

def next_monster(monster_list:list):

    assert type(monster_list) is list
    if len(monster_list)>0:
        return monster_list[0]


if __name__=='__main__':
    main()

# 结果
# 请输入英雄姓名：zxw
# 请输入英雄种族：
# 1.人族 2.精灵族
# 1
# --------------------------------------------------
# 战斗开始
# --------------------------------------------------
# 遇到第1只怪兽
# ******************** round 1 ********************
# 护盾受到3点攻击
# 护盾受到4点攻击
# Name:zxw	 HP:100	 Level:1	 shield:16
# Name:咸鱼	 HP:20	 Level:1	 shield:7
# ******************** round 2 ********************
# 护盾受到5点攻击
# 护盾受到7点攻击
# Name:zxw	 HP:100	 Level:1	 shield:9
# Name:咸鱼	 HP:20	 Level:1	 shield:2
# ******************** round 3 ********************
# 护盾受到1点攻击
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:1	 shield:9
# Name:咸鱼	 HP:20	 Level:1	 shield:1
# ******************** round 4 ********************
# 英雄向怪兽发动攻击
# 怪兽受到10点伤害
#
# 咸鱼的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:1	 shield:9
# Name:咸鱼	 HP:10	 Level:1	 shield:-9
# ******************** round 5 ********************
# 英雄向怪兽发动攻击
# 怪兽受到3点伤害
#
# 咸鱼的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:1	 shield:9
# Name:咸鱼	 HP:7	 Level:1	 shield:-12
# ******************** round 6 ********************
# 英雄向怪兽发动攻击
# 怪兽受到1点伤害
#
# 咸鱼的护盾破裂！
# 护盾受到2点攻击
# Name:zxw	 HP:100	 Level:1	 shield:7
# Name:咸鱼	 HP:6	 Level:1	 shield:-13
# ******************** round 7 ********************
# 英雄向怪兽发动攻击
# 怪兽受到6点伤害
#
# 咸鱼的护盾破裂！
# Name:zxw	 HP:100	 Level:1	 shield:7
# Name:咸鱼	 HP:0	 Level:1	 shield:-19
# --------------------------------------------------
# zxw获得了胜利，获得了大量经验值
# ---------- zxw升到了2级！ ----------
# --------------------------------------------------
# 遇到第2只怪兽
# ******************** round 1 ********************
# 英雄向怪兽发动攻击
# 怪兽受到13点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:67	 Level:1	 shield:-3
# ******************** round 2 ********************
# 英雄向怪兽发动攻击
# 怪兽受到9点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:58	 Level:1	 shield:-12
# ******************** round 3 ********************
# 英雄向怪兽发动攻击
# 怪兽受到1点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:57	 Level:1	 shield:-13
# ******************** round 4 ********************
# 英雄向怪兽发动攻击
# 怪兽受到11点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:46	 Level:1	 shield:-24
# ******************** round 5 ********************
# 英雄向怪兽发动攻击
# 怪兽受到11点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:35	 Level:1	 shield:-35
# ******************** round 6 ********************
# 英雄向怪兽发动攻击
# 怪兽受到4点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:31	 Level:1	 shield:-39
# ******************** round 7 ********************
# 英雄向怪兽发动攻击
# 怪兽受到10点伤害
#
# 牛头人的护盾破裂！
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:100	 Level:2	 shield:7
# Name:牛头人	 HP:21	 Level:1	 shield:-49
# ******************** round 8 ********************
# 英雄向怪兽发动攻击
# 怪兽受到14点伤害
#
# 牛头人的护盾破裂！
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到8了攻击！
#
# Name:zxw	 HP:92	 Level:2	 shield:-1
# Name:牛头人	 HP:7	 Level:1	 shield:-63
# ******************** round 9 ********************
# 英雄向怪兽发动攻击
# 怪兽受到12点伤害
#
# 牛头人的护盾破裂！
# Name:zxw	 HP:92	 Level:2	 shield:-1
# Name:牛头人	 HP:-5	 Level:1	 shield:-75
# --------------------------------------------------
# zxw获得了胜利，获得了大量经验值
# ---------- zxw升到了3级！ ----------
# --------------------------------------------------
# 遇到第3只怪兽
# ******************** round 1 ********************
# 英雄向Boss发动攻击
# Boss受到10点伤害
#
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到12了攻击！
#
# Name:zxw	 HP:80	 Level:3	 shield:-13
# Name:魔王	 HP:100	 Level:3	 shield:20
# ******************** round 2 ********************
# 英雄向Boss发动攻击
# Boss受到10点伤害
#
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到4了攻击！
#
# Name:zxw	 HP:76	 Level:3	 shield:-17
# Name:魔王	 HP:100	 Level:3	 shield:10
# ******************** round 3 ********************
# 英雄向Boss发动攻击
# Boss受到25点伤害
#
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到6了攻击！
#
# Name:zxw	 HP:70	 Level:3	 shield:-23
# Name:魔王	 HP:75	 Level:3	 shield:-15
# ******************** round 4 ********************
# 英雄向Boss发动攻击
# Boss受到10点伤害
#
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到12了攻击！
#
# Name:zxw	 HP:58	 Level:3	 shield:-35
# Name:魔王	 HP:65	 Level:3	 shield:-25
# ******************** round 5 ********************
# 英雄向Boss发动攻击
# Boss受到23点伤害
#
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:58	 Level:3	 shield:-35
# Name:魔王	 HP:42	 Level:3	 shield:-48
# ******************** round 6 ********************
# 英雄向Boss发动攻击
# Boss受到25点伤害
#
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:58	 Level:3	 shield:-35
# Name:魔王	 HP:17	 Level:3	 shield:-73
# ******************** round 7 ********************
# 英雄向Boss发动攻击
# Boss受到0点伤害
#
# 怪兽向zxw攻击，但被zxw躲避了攻击！
#
# Name:zxw	 HP:58	 Level:3	 shield:-35
# Name:魔王	 HP:17	 Level:3	 shield:-73
# ******************** round 8 ********************
# 英雄向Boss发动攻击
# Boss受到9点伤害
#
# 护盾破裂！
# 怪兽向zxw攻击
# zxw受到3了攻击！
#
# Name:zxw	 HP:55	 Level:3	 shield:-38
# Name:魔王	 HP:8	 Level:3	 shield:-82
# ******************** round 9 ********************
# 英雄向Boss发动攻击
# Boss受到8点伤害
#
# Name:zxw	 HP:55	 Level:3	 shield:-38
# Name:魔王	 HP:0	 Level:3	 shield:-90
# --------------------------------------------------
# zxw获得了胜利，获得了大量经验值
# 因为zxw已满级不能在获得更多的经验值！
# 恭喜zxw通关了游戏