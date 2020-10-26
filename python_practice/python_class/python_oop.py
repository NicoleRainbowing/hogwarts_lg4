# -*- coding: UTF-8 -*-
# @Time     :2020/10/24 
# @Author   :NicoleRW
#@File      :python_oop.py

#类名和变量名命名一样
#类名需要用驼峰式，第一个字母要大写
#面型对象
class HouseLei:
    # 类属性
    # 类的静态属性、类变量
    # 在类之中，在方法之外
    door = "red"
    floor = "white"

    def __init__(self):
        #构造函数，在类实例化的时候直接执行
        #在方法中，调用类变量需要加self
        #不写也会自动生成
        print(self.door)
        #定义实例变量，需要加self.
        #在类当中，在方法当中
        self.kitchen = "cook"

    # 动态方法
    # 类方法
    # 所有的方法必须传一个self
    def sleep(self):
        # 普通变量：在类的方法当中，前面没有self
        bed = "席梦思"
        # f 是插值的方法，可以直接做变量的引用
        print(f"可以在房子里可以躺在{bed}上睡觉")
        # 在普通方法中的实例变量
        self.tabole = "桌子可以放东西"

    def cook(self):
        # 在方法中可以直接调用实例变量
        print(self.kitchen)
        print("在房子里可以吃饭")
        print(self.tabole)

#把类实例化:可以访问和修改类中的属性
#北欧风格的房子
north_house = HouseLei()
#中式风格的房子
china_house = HouseLei()

# 0、属性调用
#调用类属性
print(HouseLei.door)
#实例对象调用类属性
print(north_house.door)

# 一、第一个变相变相练习

# #1、修改类属性
# HouseLei.door = "white"
# print(HouseLei.door)
# print(north_house.door)
# print(china_house.door)
#
# #2、通过对象修改类属性，因为指向的内存空间是不一样的
# north_house.door = "black"
# print(HouseLei.door)
# print(north_house.door)
# print(china_house.door)

#3、普通变量、实例变量（要加载构造函数中）
north_house.sleep()
#如果不执行sleep直接执行cook，会AttributeError: 'HouseLei' object has no attribute 'tabole'
# 因为没有没有实例化
north_house.cook()

#4、self是什么？
# self作为方法的第一个参数传进去，self就是作为默认的，你喜欢的话可以改个名字写个别的
# 一般都写self方便辨认