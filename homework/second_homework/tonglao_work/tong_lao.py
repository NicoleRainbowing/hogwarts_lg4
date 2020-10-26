# -*- coding: UTF-8 -*-
# @Time     :2020/10/26 
# @Author   :NicoleRW
# @File      :tong_lao.py

'''
作业2
加入模块化改造
'''


# 天山童姥类:属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
class TongLao():

    # 构造器
    def __init__(self, blood, power):
        # 血量
        self.blood = blood
        # 武力值
        self.power = power

    '''
    see_people方法，需要传入一个name参数，
    如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
    如果传入“李秋水”，打印“师弟是我的！”，
    如果传入“丁春秋”，打印“叛徒！我杀了你”
    '''
    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            pass

    '''
    fight_zms方法（天山折梅手），
    调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    需要传入敌人的hp，power，进行一回合制对打，
    打完之后，比较双方血量。血多的一方获胜。
    '''
    def __fight_zms(self, hp, enemy_power):
        self.power = self.power * 10
        self.blood = self.blood / 2
        self.blood = self.blood - enemy_power
        enemy_power = enemy_power - self.blood
        if enemy_power > hp :
            print("你居然赢了我！")
        elif enemy_power < hp:
            print("哈哈哈哈，果然是我！我赢了")
        else:
            print("能够和我不分胜负，你也有两把刷子")
