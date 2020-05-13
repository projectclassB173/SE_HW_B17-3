import random

sheld=10
class human():
    def __init__(self,name):
        self.NAME=name
        self.LV=1
        self.MAXHp=self.LV*50
        self.HP=self.LV*50
        self.DEX=0.8
        self.DEF=0
    def LVUP(self):
        self.LV+=1
        self.HP=self.LV*50
        self.MAXHp=self.LV*50
        if self.LV<=3:
            print("     玩家{} 升级,LV {},HP {}".format(self.NAME, self.LV, self.HP))
        else:
            print("     玩家{}已满级".format(self.NAME))
class elf:
    def __init__(self,name):
        self.NAME=name
        self.LV=1
        self.MAXHp=self.LV*50
        self.HP=self.LV*50
        self.STR=random.randint(1,15)*self.LV
        self.DEX=0.5
        self.DEF=0
    def LVUP(self):
        self.LV+=1
        self.HP=self.LV*50
        self.MAXHp=self.LV*50
        if self.LV<=3:
            print("     玩家{} 升级,LV {},HP {}".format(self.NAME, self.LV, self.HP))
        else:
            print("     玩家{}已满级".format(self.NAME))

class monster:
    def __init__(self,name,level):
        self.NAME=name
        self.LV=level
        self.MAXHp=self.LV*20
        self.HP=self.LV*20
        self.STR=random.randint(1,10)*self.LV
        self.DEX=0
        self.DEF=0
class boss:
    def __init__(self,name):
        self.NAME=name
        self.LV=3
        self.MAXHp=self.LV*50
        self.HP=self.LV*50
        self.STR=random.randint(1,10)*self.LV
        self.DEX=0
        self.MAXDEF=10
        self.DEF=10


def action(NAME1,NAME2,STR1,DEX2,DEF2,HP2):
    if DEX2>random.randint(0,1):
        print("     {} 攻击 {} 但攻击miss了！".format(NAME1,NAME2))
    else:
        if DEF2<=0:
            str=STR1
            HP2-=str
            print("     {} 攻击 {} 命中，造成了 {} 点伤害".format(NAME1,NAME2,str))
        else:
            str=STR1
            if STR1>=DEF2:
                STR1-=DEF2
                HP2-=STR1
                print("     {} 攻击 {} 命中，对护盾造成了 {} 点伤害".format(NAME1,NAME2,str))
                print("     护盾被打破了！")
                global sheld
                sheld=0
            else:
                print("     {} 攻击 {} 命中，对护盾造成了 {} 点伤害，伤害不足下回合护盾值将回满".format(NAME1,NAME2,str))
    return HP2


def main():
    playerName=input("请输入角色名：")
    playerRace=input("请输入种族(1、elf 2、human)：")
    if playerRace=="1":
        hero=elf(playerName)
    elif playerRace=="2":
        hero=human(playerName)
    else:
        print("您输入的种族不存在，请重启程序重新输入")
    m1=monster("杂鱼a",1)
    m2=monster("干部b",2)
    m3=boss("boss")
    ms=[m1,m2,m3]
    round=1
    heroN=1
    monN=3
    while heroN and monN:
        print("     =====第{}回合=====".format(round))
        ms[0].HP=action(hero.NAME,ms[0].NAME,random.randint(1,15)*hero.LV,ms[0].DEX,ms[0].DEF,ms[0].HP)
        if sheld==0:
            m3.DEF=0
        if ms[0].HP<=0:
            print("     {} 阵亡".format(ms[0].NAME))
            hero.LVUP()
            ms[0].HP=0
            del ms[0]
            monN-=1

        if len(ms)==0:
            print("     {} 胜利".format(hero.NAME))
            return
        for num in range(0,monN):
            hero.HP=action(ms[num].NAME,hero.NAME,random.randint(1,10)*ms[num].LV,hero.DEX,hero.DEF,hero.HP)
        if hero.HP<=0:
            print("     {} 胜利".format(m3.NAME))
            heroN-=1
            return
        print('\t')
        print("     LV{}的{}的血量是{}/{}".format(hero.LV,hero.NAME,hero.HP,hero.MAXHp))
        if m1.HP:
            print("     LV{}的{}的血量是{}/{}".format(m1.LV,m1.NAME,m1.HP,m1.MAXHp))
        if m2.HP:
            print("     LV{}的{}的血量是{}/{}".format(m2.LV,m2.NAME,m2.HP,m2.MAXHp))
        print("     LV{}的{}的血量是{}/{}，护盾值{}/{}".format(m3.LV,m3.NAME,m3.HP,m3.MAXHp,m3.DEF,m3.MAXDEF))
        print('\t')
        round+=1

if __name__ == '__main__':
    main()

