# # 单继承
# class human(object):
#     def info(self):
#         print('human')
# class man(human): # 继承human
#     pass
# Jack=man()
# Jack.info()

# # 多继承
# class woman:
#     def info(self):
#         print('woman')
# class child(human,woman):
#     pass
# Tom=child()
# Tom.info()
# # human
# # 若human在woman前面，则遇到相同的方法使用前面的
# # 子类的魔法属性__mro__决定了属性和方法的查找顺序
# print(child.__mro__)

# # 子类重写父类的方法
# class human(object):
#     def info(self):
#         print('human')
# class man(human):
#     def info(self): # 若子类有和父类同名属性和方法，则默认用子类的
#         print('man')
#     # 子类调用父类的方法
#     # 可通过__init__方法来修改self的属性值和方法
#     # 无论何时何地，self都表示是子类的对象。
#     # 在调用父类方法时，通过传递self参数，来控制方法和属性的访问修改。
#     def human_info(self):
#         print("执行__init__方法前:")
#         self.info()
#         # 调用父类方法格式：父类类名.父类方法(self)
#         human.__init__(self)
#         print("执行__init__方法后:")
#         # 调用了父类Master的实例方法
#         human.info(self)
# Jary=man()
# Jary.info() # man
# Jary.human_info()

# #  super()
# # 子类继承了多个父类，如果父类类名修改了，那么子类也要涉及多次修改。而且需要重复写多次调用，显得代码臃肿。
# # 使用super()可以逐一调用所有的父类方法，并且只执行一次。调用顺序遵循mro类属性的顺序。
# # 注意：如果继承了多个父类，且父类都有同名方法，则默认只执行第一个父类的
# # (同名方法只执行一次，目前super()不支持执行多个父类的同名方法)
# # super()在Python2.3之后才有的机制，用于通常单继承的多层继承。
# class human(object):
#     def info(self):
#         print('human')
# class man(human):
#     def info(self):
#         print('man')
#     def human_info(self):
#         super().__init__()
#         super().info() #  执行父类的实例方法
#         self.info() # 执行本类的实例方法
# zhangsan=man()
# zhangsan.human_info()

