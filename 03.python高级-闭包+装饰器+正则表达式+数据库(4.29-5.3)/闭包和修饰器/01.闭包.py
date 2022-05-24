# def man1(x):
#     # 在函数内部再定义函数
#     def marry(y):
#         # 内部函数使用了外部函数的变量
#         print("%s想和%s结婚"%(x,y))
#     # 外部函数返回了内部函数
#     return marry
#
# ZS = man1("张三")
# #即man函数结束后，返回的marry被ZS保存，并且marry仍保存了man函数的参数"张三"
# ZS("李四")
# ZS("王五")

# def man2(x):
#     # 在函数内部再定义函数
#     def marry(y):
#         # 这里本意想要修改外部x的值，实际上是在内部函数定义了一个局部变量x
#         x = x+"的朋友"
#         # 内部函数使用了外部函数的变量
#         print(x+"和"+y+"结婚")
#     # 外部函数返回了内部函数
#     return marry
#
# ZS = man2("张三")
# #即man函数结束后，返回的marry被ZS保存，并且marry仍保存了man函数的参数"张三"
# ZS("李四")
# ZS("王五")

# def man3(x):
#     # 在函数内部再定义函数
#     def marry(y):
#         # 这里本意想要修改外部x的值，实际上是在内部函数定义了一个局部变量x
#         nonlocal x  # 告诉解释器，此处使用的是 外部变量x
#         # 修改外部变量x
#         x = x+"的朋友"
#         # 内部函数使用了外部函数的变量
#         print(x+"和"+y+"结婚")
#     # 外部函数返回了内部函数
#     return marry
#
# ZS = man3("张三")
# #即man函数结束后，返回的marry被ZS保存，并且marry仍保存了man函数的参数"张三"
# ZS("李四")
# ZS("王五")
