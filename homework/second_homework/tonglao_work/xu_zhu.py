# -*- coding: UTF-8 -*-
# @Time     :2020/10/26 
# @Author   :NicoleRW
#@File      :xu_zhu.py

from homework.second_homework.tonglao_work.tong_lao import TongLao

'''
定义一个XuZhu类，继承于童姥。
虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。
每次调用都会打印“罪过罪过”
'''



class XuZhu(TongLao):

    # 念经方法
    def read(self):
        print("罪过罪过")