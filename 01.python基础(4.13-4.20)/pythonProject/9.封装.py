# # 私有权限：在属性名和方法名前加上两个下划线：__
# # Python中没有像C++中 public 和 private 这些关键字来区别公有属性和私有属性。
# # Python是以属性命名方式来区分，如果在属性和方法名前面加了2个下划线'__'，则表明该属性和方法是私有权限，否则为公有权限
# class master(object):
#     def __init__(self):
#         self.__kongfu='大师'
#     def get_kongfu(self): # 现代软件开发中，通常会定义get_xxx()方法和set_xxx()方法来获取和修改私有属性值。
#         return self.__kongfu
#     def set_kongfu(self,str):
#         self.__kongfu=str
#     def  __info(self):
#         print('__info() 执行') # 和C++相同
#     def get_info(self):
#         self.__info()
# Tom=master()
# print(Tom.get_kongfu())
# Tom.get_info()
# Tom.set_kongfu('王者')
# print(Tom.get_kongfu())
