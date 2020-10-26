# -*- coding: UTF-8 -*-
# @Time     :2020/10/26
# @Author   :NicoleRW
#@File      :describe_oop.py

'''
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个。
设计：
人类，静态属性为人种、性别，方法有成长
女孩继承人类，静态属性性别重写为female，方法早恋、分手、年龄增长
男孩继承人类，静态属性性别重写为male，方法
男朋友继承男孩，女孩说分手，就变成单身狗，年龄成长
单身狗继承男孩，女孩恋爱了就变成男朋友，年龄增长
'''

# 人类
class Human():
    #类（人）的静态属性，类变量
    #人种
    race = ["white","yellow","black"]
    #性别
    gender = ["male","female"]

    # （人）类的构造函数
    def __init__(self,name):
        #出生年龄为0岁
        self.age = 0
        self.name = name

    # 长大方法
    def grow_up(self,suffering):
        self.age = self.age + suffering

# 女孩类
class Girl(Human):
    #类（女孩）的静态属性，类变量
    gender = "female"

    #类（女孩）的构造函数
    def __init__(self,name):
        # Pycham让我加的？为啥？？
        super().__init__(name)
        # 胸
        self.breath = ["34C"]

    # 早恋方法，年满18岁就发男朋友
    def puppy_love(self):
        not_single = False
        #年满18岁就给发个男朋友
        if self.age >= 18:
            print("我有男朋友啦！")
            not_single = True
        return not_single

    # 分手方法
    def break_up(self):
        print("我没有男朋友啦！")

class Boy(Human):
    #类（男孩）的静态变量，男的
    gender = "male"

    def __init__(self,name):
        super().__init__(name)
        self.breath = ["chest"]

# 男朋友类
class Boyfriend(Boy):
    #类（男朋友）的静态变量，类变量

    def __init__(self, name,Human):
        super().__init__(name)
        self.girl = Human.name

    # 男朋友的关心
    def care_for(self):
        return "多喝热水"

    # 男朋友过节
    def double_eleven(self):
        return f"双十一啦，我要给{self.girl}买买买！"

class SingleDog(Boy):

    # 单身狗的过节方法
    def double_eleven(self):
        return "我过光棍儿节来啦~"

# 介绍类
class SelfIntroduction():
    def self_introduction(self,name,**kw):
        #介绍名字
        print(f"我的名字叫{name}。")
        #介绍我的其他信息
        for key in kw :
            print(f"我的{key}是{kw[key]}")

    def story_introduction(self,**kw):
        #介绍我经历的说的话
        for key in kw :
            print(f"我在{key}的时候，说：{kw[key]}")

    def auto_introduction(self,Human):
        self.self_introduction(Human.name, gender=Human.gender, type=Human.__class__.__name__)
        self.story_introduction(double_eleven=Human.double_eleven())


if __name__ == '__main__':
    # 实例化类
    # 实例化一个单身狗：小明
    Xiao_ming = SingleDog("小明")
    # 实例化一个女孩：赫敏Hermione
    Hermione = Girl("Hermione")
    # 实例化一个男朋友:罗恩Ron
    Ron_Weasley = Boyfriend("Ron_Weasley",Hermione)
    # 实例化一次自我介绍：第一次见面
    first_meet = SelfIntroduction()

    #单身狗的自我介绍
    first_meet.auto_introduction(Xiao_ming)
    #男朋友的自我介绍
    first_meet.auto_introduction(Ron_Weasley)

