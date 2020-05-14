from random import randint
from Hero import Person


class Monster(Person):
      def __init__(self,name,hp=20,level=1,shield=10):
          super().__init__(name,hp,level,shield)

      def attack(self,hero):
          if self.level==1:
              hurt=randint(0,10)
          if self.level==2:
              hurt=randint(0,20)
          hero.defence(hurt)

      def defence(self,hurt):
          self.shield -= hurt
          if self.shield <= 0:
              self._hp -= hurt

              print('英雄向怪兽发动攻击\n怪兽受到{}点伤害\n'.format(hurt))
              print("{}的护盾破裂！".format(self.get_name()))
          else:
              print("护盾受到{}点攻击".format(hurt))



class Boss(Person):
    def __init__(self,name,hp):
        super().__init__(name,hp,3,shield=50)
        self.shield=30 #盾牌
    def attack(self,hero):
        hurt=randint(0,30)
        hero.defence(hurt)
    def defence(self,hurt):
        self.shield -= hurt
        if self.shield<=0:
            self._hp -= hurt
        print('英雄向Boss发动攻击\nBoss受到{}点伤害\n'.format(hurt))







