import random as n

# 英雄具有两个可选种族，人类和精灵
# 主角（人类和精灵）
class Role:
    # 属性
    def __init__(role, name):
        role.name = name                       # 实例属性：名字
        role.level = 1                         # 级别（共3级）
        role.life = role.level * 60            # 当前生命
        role.maxlife = role.level * 60         # 当前等级的最大生命
    # 定义实例方法：攻击
    def attack(role):
        R_attack = n.randint(0, role.level*10)
        print("—{0}发动攻击".format(role.name))
        return R_attack
    # 升级
    def upgrade(role):
        role.life = role.life + 10             # 英雄升级时当前血量加10
        role.level = role.level + 1            # 等级加1
        print("—{0}升级，当前等级{1}，当前血量{2}！".format(role.name, role.level, role.life)) # 访问类变量
    # 防御
    def defense(role, R_attack):
        X_flexibility = n.random()             # 产生一个随机数，如果小于灵活性则躲避，大于灵活性则命中
        if role.flexibility < X_flexibility:
            role.life = role.life - R_attack
            if role.life < 0:                  # 英雄血量低于0时，显示为0
                role.life = 0
            print("——{0}受到{1}点伤害，当前血量{2}".format(role.name, R_attack, role.life))
        else:
            print("——{0}躲避了本次攻击！".format(role.name))

# 人类灵活性
class Human(Role):
    # 属性
    def __init__(role, name):
        super(Human, role).__init__(name)
        role.flexibility = 0.4                 # 人类闪避率为40%
# 精灵灵活性
class Spirit(Role):
    # 属性
    def __init__(role, name):
        super(Spirit, role).__init__(name)
        role.flexibility = 0.8                 # 精灵闪避率为80%

#小怪兽
class Monster:
    # 属性
    def __init__(monster, name, level):
        monster.name = name                    # 名字
        monster.level = level                  # 级别
        monster.life = int(level * 20)         # 当前生命
        monster.maxlife = int(level * 20)      # 当前等级的最大生命
    # 攻击
    def attack(monster):
        R_attack = n.randint(0, monster.level * 10)
        print("—{0}发动攻击".format(monster.name))
        return R_attack
    # 防御
    def defense(monster, R_attack):
        monster.life = monster.life - R_attack
        if monster.life < 0:                   # 小怪兽血量低于0时，显示为0
            monster.life = 0
        print("——{0}受到{1}点伤害，当前血量 {2}".format(monster.name, R_attack, monster.life))

# 大怪兽
class Big_Monster(Monster):
    # 属性
    def __init__(monster_boss, name, level):
        monster_boss.name = name
        super(Big_Monster, monster_boss).__init__(name, level)
        monster_boss.protect = monster_boss.maxlife * 0.6  # 设置护盾值为大怪兽血量的60%
    # 防御
    def defense(monster_boss, R_attack):       # 大怪兽受到攻击时先扣除护盾，护盾为0时扣除血量
        if monster_boss.protect > 0:
            monster_boss.protect = monster_boss.protect - R_attack
            if monster_boss.protect < 0:       # 大怪兽护盾低于0时，显示为0
                monster_boss.protect = 0
            print("——{0}受到{1}点伤害，当前护盾值{2}，血量{3}".format(monster_boss.name, R_attack, monster_boss.protect, monster_boss.life))
        else:
            monster_boss.life = monster_boss.life - R_attack
            if monster_boss.life < 0:          # 大怪兽血量低于0时，显示为0
                monster_boss.life = 0
            print("——{0}受到{1}点伤害，当前护盾值{2}，血量{3}".format(monster_boss.name, R_attack, monster_boss.protect, monster_boss.life))

# 主函数
def main():
    # 选择生成英雄的种族，人类或精灵
    hero = int(input("请选择英雄的种族——1人类；2精灵："))
    if(hero == 1):
        role = Human("人类")
    elif(hero == 2):
        role = Spirit("精灵")
    else:
        print("选择错误，请输入1或者2")
        return
    # 生成两个小怪兽和一个大怪兽
    monster1 = Monster("小怪兽1号", 1)
    monster2 = Monster("小怪兽2号", 2)
    monster_boss = Big_Monster("怪兽Boss", 3)
    MonsterNum = [monster1, monster2, monster_boss]
    n = 1
    while True:
        print("第{0}回合：".format(n))
        MonsterNum[0].defense(role.attack())   # 依照次序依次攻击monster1, monster2, monster_boss
        if MonsterNum[0].life <= 0:
            print("—{0}阵亡了！".format(MonsterNum[0].name))
            role.upgrade()                     # 当击败怪兽时英雄会升级
            del MonsterNum[0]
        if len(MonsterNum) == 0:               # 没有怪兽时英雄Win
            print("==英雄Win！==")
            return
        for each in MonsterNum:
            role.defense(each.attack())
        if role.life == 0:                     # 英雄血量为0时Lose
            print("==英雄Lose！==")
            return
        n = n + 1                              # 回合数加1

# 执行
if __name__ == '__main__':
    print("——打怪兽小游戏开始！——")
    main()
    print("——游戏结束！——")





================= RESTART: D:\课程\大三下\项目实战\课后作业\Python\打怪兽小游戏.py ================
——打怪兽小游戏开始！——
请选择英雄的种族——1人类；2精灵：1
第1回合：
—人类发动攻击
——小怪兽1号受到0点伤害，当前血量 20
—小怪兽1号发动攻击
——人类受到5点伤害，当前血量55
—小怪兽2号发动攻击
——人类躲避了本次攻击！
—怪兽Boss发动攻击
——人类受到11点伤害，当前血量44
第2回合：
—人类发动攻击
——小怪兽1号受到2点伤害，当前血量 18
—小怪兽1号发动攻击
——人类受到9点伤害，当前血量35
—小怪兽2号发动攻击
——人类受到7点伤害，当前血量28
—怪兽Boss发动攻击
——人类受到21点伤害，当前血量7
第3回合：
—人类发动攻击
——小怪兽1号受到3点伤害，当前血量 15
—小怪兽1号发动攻击
——人类受到1点伤害，当前血量6
—小怪兽2号发动攻击
——人类受到17点伤害，当前血量0
—怪兽Boss发动攻击
——人类受到23点伤害，当前血量0
==英雄Lose！==
——游戏结束！——
>>> 
================= RESTART: D:\课程\大三下\项目实战\课后作业\Python\打怪兽小游戏.py ================
——打怪兽小游戏开始！——
请选择英雄的种族——1人类；2精灵：2
第1回合：
—精灵发动攻击
——小怪兽1号受到7点伤害，当前血量 13
—小怪兽1号发动攻击
——精灵躲避了本次攻击！
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第2回合：
—精灵发动攻击
——小怪兽1号受到8点伤害，当前血量 5
—小怪兽1号发动攻击
——精灵躲避了本次攻击！
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第3回合：
—精灵发动攻击
——小怪兽1号受到2点伤害，当前血量 3
—小怪兽1号发动攻击
——精灵躲避了本次攻击！
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵受到14点伤害，当前血量46
第4回合：
—精灵发动攻击
——小怪兽1号受到2点伤害，当前血量 1
—小怪兽1号发动攻击
——精灵受到4点伤害，当前血量42
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第5回合：
—精灵发动攻击
——小怪兽1号受到8点伤害，当前血量 0
—小怪兽1号阵亡了！
—精灵升级，当前等级2，当前血量52！
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第6回合：
—精灵发动攻击
——小怪兽2号受到12点伤害，当前血量 28
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第7回合：
—精灵发动攻击
——小怪兽2号受到16点伤害，当前血量 12
—小怪兽2号发动攻击
——精灵躲避了本次攻击！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第8回合：
—精灵发动攻击
——小怪兽2号受到19点伤害，当前血量 0
—小怪兽2号阵亡了！
—精灵升级，当前等级3，当前血量62！
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第9回合：
—精灵发动攻击
——怪兽Boss受到16点伤害，当前护盾值20.0，血量60
—怪兽Boss发动攻击
——精灵受到10点伤害，当前血量52
第10回合：
—精灵发动攻击
——怪兽Boss受到7点伤害，当前护盾值13.0，血量60
—怪兽Boss发动攻击
——精灵受到13点伤害，当前血量39
第11回合：
—精灵发动攻击
——怪兽Boss受到2点伤害，当前护盾值11.0，血量60
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第12回合：
—精灵发动攻击
——怪兽Boss受到14点伤害，当前护盾值0，血量60
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第13回合：
—精灵发动攻击
——怪兽Boss受到14点伤害，当前护盾值0，血量46
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第14回合：
—精灵发动攻击
——怪兽Boss受到22点伤害，当前护盾值0，血量24
—怪兽Boss发动攻击
——精灵受到21点伤害，当前血量18
第15回合：
—精灵发动攻击
——怪兽Boss受到1点伤害，当前护盾值0，血量23
—怪兽Boss发动攻击
——精灵躲避了本次攻击！
第16回合：
—精灵发动攻击
——怪兽Boss受到25点伤害，当前护盾值0，血量0
—怪兽Boss阵亡了！
—精灵升级，当前等级4，当前血量28！
==英雄Win！==
——游戏结束！——
>>> 

