import random

class Person(object):
   def _init_ (self,name,hp,level):
      self.name = name
      self.max = hp
      self._hp = hp
      self.level = level

   def get_name(self):
      return self.name

   def get_hp(self):
      return self._hp

   def get_level(self):
      return self.level

   def attack(self):
      return NotImplementedError

   def _str_(self):
      return 'Name:{}\t HP:{}\t Level:{}\t'.format(self.name, self._hp, self.level)

class Hero(Person):
   def _init_ (self,name,hp=20,level=1,race='human'):
      super()._init_(name,hp,level)
      self.race = race
      if self.race =='human':
         self.agile =0.4
      if self.race =='fairy':
         self.agile =0.8

   def attack(self,monster):
      if self.level == 1:
         hurt = random.randint(0,3)
      elif self.level == 2:
         hurt = random.randint(2,5)
      elif self.level == 3:
         hurt = random.randint(4,7)
      monster.defence(hurt)

   def defence(self,hurt):
      luck =random.random()
      if luck >= self.agile:
         self._hp -=hurt
         print('你受到{}点攻击'.format(hurt))
     else:
         print('你躲避了攻击')

   def upgrade(self):
      self.level +=1
      self.max = self.max +10
      self._hp = self.max
      print('你升级到{}级'.format(self.level))



class orc(Person):
      def _init_ (self,name,hp=20,level=1):
      super()._init_(name,hp,level)
   def attack(self,hero):
      if self.level == 1:
         hurt = random.randint(0,3)
      elif self.level == 2:
         hurt = random.randint(2,5)

   def defence(self,hurt):
      self._hp -= hurt
      print('兽人受到{}点攻击'.format(hurt))

class elite_orc(Person):
      def _init_ (self,name,hp=30,level=1):
      super()._init_(name,hp,level)
   def attack(self,hero):
      if self.level == 1:
         hurt = random.randint(3,6)
      elif self.level == 2:
         hurt = random.randint(5,8)

   def defence(self,hurt):
      self._hp -= hurt
      print('精英兽人受到{}点攻击'.format(hurt))

class boss_orc(Person):
      def _init_ (self,name,hp=80):
      super()._init_(name,hp)
   def attack(self,hero):
      hurt = randint(10,20)
      hero.denfence(hurt)

   def defence(self,hurt):
      self._hp -= hurt
      print('Boss受到{}点攻击'.format(hurt))




def main():
      hero =Hero('DDJ',100,1,'human')
      orc = orc('兽人',20,1)
      elite = elite_orc('精英兽人',30,1)
      boss = boss_orc('Boss',100)
      monster_list = [orc,elite,boss]
      round = 1
      while hero.get_hp() > 0 and len(monster_list) >0:
      monster = next_monster(monster_list)
      while monster.get_hp() > 0:
         print('战斗回合{}'.format(round))
         hero.attack(monster)
         if monster.get_hp() > 0:
             monster.attack(hero)
             if hero.get_hp() <=0:
                 break
       print(hero)
       print(monster)
       round += 1
   if monster.get_hp() <=0:
   monster_list.remove(monster)
     hero.upgrade()
     monster = next_monster(monster_list)

if hero.get_hp() >0:
     print('胜利,{}'.format(hero.get_name()))
else:
     print('You lose')
      

