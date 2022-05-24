# # 类方法
# # 是类对象所拥有的方法，需要用修饰器@classmethod来标识，
# # 对于类方法，第一个参数必须是类对象，一般以cls做为第一个参数
# class people(object):
#     country='China'
#     # 类方法
#     @classmethod
#     def get_country(cls): # 通过类方法访问类属性
#         return cls.country
#     @classmethod
#     def set_country(cls,country):  # 通过类方法修改类属性
#         cls.country=country
# p=people()
# print('通过实例对象引用：%s'%p.get_country()) # 可以通过实例对象来引用
# print('通过类对象引用：%s'%people.get_country()) # 也可以通过类对象引用
# p.set_country('河南')
# print(p.get_country())

# # 静态方法
# # 通过修饰器@staticmethod来修饰，静态方法不需要多定义参数，可以通过对象和类来访问
# class people(object):
#     country='china'
#     @staticmethod
#     def get_country(): # 不需要参数，直接使用类名进行访问
#         return people.country
# p=people()
# print(p.get_country()) # 通过对象访问静态方法
# print(people.get_country())# 通过类访问静态方法
#
# # 从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
# # 实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
# # 静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类实例对象来引用

