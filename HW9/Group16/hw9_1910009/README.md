# 面向对象编程练习

## 题目

编写一个打怪兽的小游戏。
游戏要求如下：

1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，直到有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

## 运行结果

```
******************** fighting of round 1 ********************
Monster受到10点伤害
你受到0点攻击
Name:Asahi 	 HP: 100 	 Level:  1
Name:Monster1 	 HP:  50 	 Level:  1
******************** fighting of round 2 ********************
Monster受到7点伤害
你受到6点攻击
Name:Asahi 	 HP:  94 	 Level:  1
Name:Monster1 	 HP:  43 	 Level:  1
******************** fighting of round 3 ********************
Monster受到2点伤害
你躲避了攻击！
Name:Asahi 	 HP:  94 	 Level:  1
Name:Monster1 	 HP:  41 	 Level:  1
******************** fighting of round 4 ********************
Monster受到8点伤害
你躲避了攻击！
Name:Asahi 	 HP:  94 	 Level:  1
Name:Monster1 	 HP:  33 	 Level:  1
******************** fighting of round 5 ********************
Monster受到4点伤害
你受到6点攻击
Name:Asahi 	 HP:  88 	 Level:  1
Name:Monster1 	 HP:  29 	 Level:  1
******************** fighting of round 6 ********************
Monster受到1点伤害
你躲避了攻击！
Name:Asahi 	 HP:  88 	 Level:  1
Name:Monster1 	 HP:  28 	 Level:  1
******************** fighting of round 7 ********************
Monster受到5点伤害
你受到8点攻击
Name:Asahi 	 HP:  80 	 Level:  1
Name:Monster1 	 HP:  23 	 Level:  1
******************** fighting of round 8 ********************
Monster受到3点伤害
你受到5点攻击
Name:Asahi 	 HP:  75 	 Level:  1
Name:Monster1 	 HP:  20 	 Level:  1
******************** fighting of round 9 ********************
Monster受到1点伤害
你受到6点攻击
Name:Asahi 	 HP:  69 	 Level:  1
Name:Monster1 	 HP:  19 	 Level:  1
******************** fighting of round 10 ********************
Monster受到2点伤害
你受到7点攻击
Name:Asahi 	 HP:  62 	 Level:  1
Name:Monster1 	 HP:  17 	 Level:  1
******************** fighting of round 11 ********************
Monster受到7点伤害
你受到7点攻击
Name:Asahi 	 HP:  55 	 Level:  1
Name:Monster1 	 HP:  10 	 Level:  1
******************** fighting of round 12 ********************
Monster受到9点伤害
你受到8点攻击
Name:Asahi 	 HP:  47 	 Level:  1
Name:Monster1 	 HP:   1 	 Level:  1
******************** fighting of round 13 ********************
Monster受到4点伤害
Name:Asahi 	 HP:  47 	 Level:  1
Name:Monster1 	 HP:  -3 	 Level:  1
你升级到了2级
******************** fighting of round 14 ********************
Monster受到15点伤害
你躲避了攻击！
Name:Asahi 	 HP: 110 	 Level:  2
Name:Monster2 	 HP:  45 	 Level:  1
******************** fighting of round 15 ********************
Monster受到16点伤害
你躲避了攻击！
Name:Asahi 	 HP: 110 	 Level:  2
Name:Monster2 	 HP:  29 	 Level:  1
******************** fighting of round 16 ********************
Monster受到2点伤害
你受到0点攻击
Name:Asahi 	 HP: 110 	 Level:  2
Name:Monster2 	 HP:  27 	 Level:  1
******************** fighting of round 17 ********************
Monster受到3点伤害
你躲避了攻击！
Name:Asahi 	 HP: 110 	 Level:  2
Name:Monster2 	 HP:  24 	 Level:  1
******************** fighting of round 18 ********************
Monster受到14点伤害
你躲避了攻击！
Name:Asahi 	 HP: 110 	 Level:  2
Name:Monster2 	 HP:  10 	 Level:  1
******************** fighting of round 19 ********************
Monster受到6点伤害
你受到5点攻击
Name:Asahi 	 HP: 105 	 Level:  2
Name:Monster2 	 HP:   4 	 Level:  1
******************** fighting of round 20 ********************
Monster受到0点伤害
你受到10点攻击
Name:Asahi 	 HP:  95 	 Level:  2
Name:Monster2 	 HP:   4 	 Level:  1
******************** fighting of round 21 ********************
Monster受到10点伤害
Name:Asahi 	 HP:  95 	 Level:  2
Name:Monster2 	 HP:  -6 	 Level:  1
你升级到了3级
******************** fighting of round 22 ********************
Boss受到7点伤害
你躲避了攻击！
Name:Asahi 	 HP: 120 	 Level:  3
Name:Boss 	 HP:  80 	 Level:  3
******************** fighting of round 23 ********************
Boss受到5点伤害
你受到30点攻击
Name:Asahi 	 HP:  90 	 Level:  3
Name:Boss 	 HP:  80 	 Level:  3
******************** fighting of round 24 ********************
Boss受到14点伤害
你受到22点攻击
Name:Asahi 	 HP:  68 	 Level:  3
Name:Boss 	 HP:  80 	 Level:  3
******************** fighting of round 25 ********************
Boss受到7点伤害
你受到5点攻击
Name:Asahi 	 HP:  63 	 Level:  3
Name:Boss 	 HP:  73 	 Level:  3
******************** fighting of round 26 ********************
Boss受到15点伤害
你受到8点攻击
Name:Asahi 	 HP:  55 	 Level:  3
Name:Boss 	 HP:  58 	 Level:  3
******************** fighting of round 27 ********************
Boss受到5点伤害
你受到0点攻击
Name:Asahi 	 HP:  55 	 Level:  3
Name:Boss 	 HP:  53 	 Level:  3
******************** fighting of round 28 ********************
Boss受到2点伤害
你受到21点攻击
Name:Asahi 	 HP:  34 	 Level:  3
Name:Boss 	 HP:  51 	 Level:  3
******************** fighting of round 29 ********************
Boss受到4点伤害
你受到2点攻击
Name:Asahi 	 HP:  32 	 Level:  3
Name:Boss 	 HP:  47 	 Level:  3
******************** fighting of round 30 ********************
Boss受到27点伤害
你躲避了攻击！
Name:Asahi 	 HP:  32 	 Level:  3
Name:Boss 	 HP:  20 	 Level:  3
******************** fighting of round 31 ********************
Boss受到8点伤害
你躲避了攻击！
Name:Asahi 	 HP:  32 	 Level:  3
Name:Boss 	 HP:  12 	 Level:  3
******************** fighting of round 32 ********************
Boss受到21点伤害
Name:Asahi 	 HP:  32 	 Level:  3
Name:Boss 	 HP:  -9 	 Level:  3
你升级到了4级
You win,Asahi
```

AsahiHuang  
2020.05.14

