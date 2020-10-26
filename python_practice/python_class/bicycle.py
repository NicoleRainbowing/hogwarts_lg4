# -*- coding: UTF-8 -*-
# @Time     :2020/10/24 
# @Author   :NicoleRW
# @File      :bicycle.py

# 自行车类
class Bicycle():
    def run(self, km):
        print(f"移动用脚丫骑了{km}公里，累死了！")


# 继承自Bicycle
# python中集成就是把父类的名称放在类名的小括号内
class EBicycle(Bicycle):
    # 属性需要传参，可以直接放在构造函数之中
    def __init__(self, valume):
        self.valume = valume

    # 充电你的房发
    def fill_charge(self, vol):
        # 充电后的电量是 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        print(f"已经冲了{vol}度电，现在电量达到了{self.valume}")

        # 骑行方法，方法重写

    def run(self, km):
        # pass怎么用：先没想好怎么写这个函数又不想报错的时候用
        # 1.得到目前电量能达到的最大里程数：电量*10
        power_km = self.valume * 10
        if power_km >= km:
            print(f"我用电骑车走完了全程{km}公里，使用了")
        else:
            # 电量不够了，电用完了以后用脚骑车
            print(f"我用电骑车了全程{power_km}公里，使用了")
            # 非继承调用，嵌套
            bike = Bicycle()
            bike.run(km - power_km)
            # 继承方式调用,父类中的方法失效了，子类的方法生效；
            # 重写不影响其他子类的效果
            super.run(km - power_km)
            # python可以继承多个，但是不推荐使用


# bike = Bicycle()
# bike.run(10)
ebike = EBicycle(10)
ebike.run(150)
