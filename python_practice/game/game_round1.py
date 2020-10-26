# -*- coding: utf-8 -*-
# @Time     :2020/10/20 
# @Author   :NicoleRW
#@File      :game_round1.py

'''
一个回合制游戏，每个角色都有hp，和power，hp代表血量，power代表攻击力
hp初始值1000，power初始值200
'''

#定义fight函数，实现游戏逻辑
def fight():
    #定义4个变量，存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    #定义最终血量计算方式
    my_final_hp = my_hp-enemy_power
    enemy_final_hp = enemy_hp-my_power

    #判断输赢
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    elif enemy_final_hp > my_final_hp :
        print("我输了")
    else:
        print("平局")