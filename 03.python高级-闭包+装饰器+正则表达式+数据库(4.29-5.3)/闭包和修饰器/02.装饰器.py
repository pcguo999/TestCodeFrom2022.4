# def add_acting(f):
#     def acting():
#         # 函数执行之前
#         print("出门")
#         f() # 被修饰的函数
#         # 函数执行之后
#         print("回家")
#     return acting
# # 使用语法糖后：
# @add_acting
# def run():
#     print("跑步")
#
# # # 使用装饰器来装饰函数，即使用add_acting函数来修饰run函数
# # run=add_acting(run)
#
# # 执行修饰后的run函数
# run()


# # 带参数的装饰器
# def add_acting(f):
#     def acting(name):
#         # 函数执行之前
#         print(name+"出门")
#         f(name) # 被修饰的函数
#         # 函数执行之后
#         print(name+"回家")
#     return acting
# # 使用语法糖后：
# @add_acting
# def run(name):
#     print(name+"跑步")
# # 执行修饰后的run函数
# run("张三")

# # 装饰带返回值的函数
# def add_acting(f):
#     def acting(x,y):
#         # 函数执行之前
#         print("开始运行：")
#         return f(x,y) # 被修饰的函数
#     return acting
# # 使用语法糖后：
# @add_acting
# def add(x,y):
#     return x+y
# # 执行修饰后的run函数
# print(add(2,3))

# # 装饰带有不定长参数的函数
# def add_acting(f):
#     def acting(*args,**kwargs):
#         # 函数执行之前
#         print("开始运行：")
#         return f(*args,**kwargs) # 被修饰的函数
#     return acting
# # 使用语法糖后：
# @add_acting
# def add(*args,**kwargs):
#     result1,result2=0,0
#     for i in args:
#         result1+=i
#     for j in kwargs.values():
#         result2+=j
#     return (result1,result2)
#
# # 执行修饰后的run函数
# print(add(2,3,x=1,y=2))

# # 多个装饰器
# def add_acting(f):
#     def acting(x,y):
#         # 函数执行之前
#         print("开始运行1：")
#         return f(x,y) # 被修饰的函数，返回结果值
#     return acting
# def add_acting2(f):
#     def acting(x,y):
#         # 函数执行之前
#         print("开始运行2：")
#         return f(x,y) # 被修饰的函数，返回结果值
#     return acting
# # 使用语法糖后：
# @add_acting
# @add_acting2
# def add(x,y):
#     return x+y
# # 执行修饰后的add函数
# print(add(2,3))

# # 带参数的装饰器
# def select(flag):
#     def add_acting(f):
#         def acting(x,y):
#             if flag==1:
#                 print("开始运行1：")
#             else:
#                 print("开始运行2：")
#             print(f(x,y))
#         return acting
#     return add_acting
#
# @select(1)
# def add(x,y):
#     return x+y
# # 执行修饰后的add函数
# add(2,3)

# # 类装饰器
# class add_acting(object):
#     def __init__(self,add):
#         self.add=add
#     def __call__(self,*args,**kwargs):
#         # 添加装饰
#         print("开始运行：")
#         self.add(*args,**kwargs) # 被修饰的函数
#
# @add_acting
# def add(*args,**kwargs):
#     result1,result2=0,0
#     for i in args:
#         result1+=i
#     for j in kwargs.values():
#         result2+=j
#     print(result1,result2)
#
# # 执行修饰后的add函数
# add(2,3,x=1,y=2)

