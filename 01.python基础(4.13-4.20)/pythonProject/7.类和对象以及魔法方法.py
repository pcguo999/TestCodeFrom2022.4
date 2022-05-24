# # python中的类分为经典类（旧式类）和新式类。python的新式类是2.2版本为了统一类和实例引进来的。
# # 在Python2.x中默认都是经典类，只有显式继承了object的才是新式类。
# # 在python3.x中取消了经典类，默认都是新式类，并且新式类不需要显式的继承object对象。如下所示，这三种写法都可以，并无区别：
# # class Hero:  # 经典类（旧式类）定义形式
# # class Hero():
# # 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
# class Hero(object):  # 新式类定义形式
#     # def __init__(self): # 类似C++的构造函数，初始化对象使用
#     #     self.name = '寒冰'  # 姓名
#     #     self.hp = 2600  # 生命值
#     #     self.atk = 450  # 攻击力
#     #     self.armor = 200  # 护甲值
#     # 带参Init函数类似C++中的复制构造函数
#     def __init__(self, name, hp, atk, armor):
#         """ __init__() 方法，用来做变量初始化 或 赋值 操作"""
#         # 英雄名
#         self.name = name
#         # 生命值：
#         self.hp = hp
#         # 攻击力
#         self.atk = atk
#         # 护甲值
#         self.armor = armor
#     def move(self):
#         print("正在前往")
#     def attack(self):
#         print("发起普通攻击")
#     # 在方法中通过self获取对象属性
#     def info(self):
#         print('英雄：%s\n生命值：%s\n攻击力：%s\n护甲值：%s'%(self.name,self.hp,self.atk,self.armor))
#     def __str__(self):
#         """
#             这个方法是一个魔法方法 ，用来显示信息
#             该方法需要 return 一个数据，并且只有self一个参数，当在类的外部 print(对象) 则打印这个数据
#         """
#         return "英雄 <%s> 数据： 生命值 %d, 攻击力 %d, 护甲值 %d" % (self.name, self.hp, self.atk, self.armor)
#     # 当对象被删除时，会自动被调用，类似C++的析构函数
#     def __del__(self):
#         print("__del__方法被调用")
#         print("%s 被干掉了..." % self.name)
# # 创建对象，实例化了一个英雄对象
# # Hanbing=Hero()
# # # 给对象添加属性以及对应的属性值
# # Hanbing.name='寒冰射手' # 姓名
# # Hanbing.hp=2600 # 生命值
# # Hanbing.atk=450 # 攻击力
# # Hanbing.armor=200 # 护甲值
#
# # #通过.成员选择运算符，获取对象的属性值
# # # print('英雄：%s\n生命值：%s\n攻击力：%s\n护甲值：%s'%(Hanbing.name,Hanbing.hp,Hanbing.atk,Hanbing.armor))
# # # # 通过.成员选择运算符，获取对象的实例方法
# # # Hanbing.move()
# # # Hanbing.attack()
# # # 在方法中通过self获取对象属性
# # Hanbing.info()
#
# GaiLun=Hero('盖伦',2500,430,250)
# # GaiLun.info()
# # 如果没有__str__ 则默认打印 对象在内存的地址。
# # 当类的实例化对象 拥有 __str__ 方法后，那么打印对象则打印 __str__ 的返回值。
# print(GaiLun)
# del GaiLun