# # python中的模块概念和C语言中的头文件以及Java的包类似
# import math
# print(sqrt(2)) # 错误
# print(math.sqrt(2)) # 正确
# # 引用模块中的函数时要加上模块名称,因为可能很多模块中含有相同名称的函数

# # 有时候我们只需要用到模块中的某个函数,只需要引入该函数就行
# from math import sqrt,sin
# # 若想一次性引入math所有的函数,也可以:
# from math import *
# # 简写用as,这样之后需要用到的可以直接m代替:
# import math as m
# from math import sqrt as sq
# print(m.sqrt())
# print(m.sq())

# # 制作自己的模块:比如test.py
#                 # def add(a,b):
#                 #     return a+b
# import test
# result=test.add(11,22)
# print(result)

# 模块中的__all__
# 模块中有__all__变量,那么也就意味着这个变量中的元素,
# 不会被from xxx import * 时导入
# from test import add as ad# 可行
# print(ad(2,3))
# from test import *
# print(min(2,3))
# print(add1(2,3))

# 包:即文件夹包将有联系的模块组织在一起，即放到同一个文件夹下，
    # 并且在这个文件夹创建一个名字为__init__.py 文件，那么
    # 这个文件夹就称之为包
# 使用:import 文件夹.模块导入
# 使用:from 文件夹 import *(模块)导入,需要在文件夹中创建__init__.py
    # 在__init__.py文件中写入__all__=["模块名1","模块名2"]
# __init__.py文件控制着包的导入行为
# 若__init__.py为空,则仅仅是把这个包导入,并不会导入包中的模块
# __init__.py中的__all__变量,控制着from 包名 import * 时导入的模块
