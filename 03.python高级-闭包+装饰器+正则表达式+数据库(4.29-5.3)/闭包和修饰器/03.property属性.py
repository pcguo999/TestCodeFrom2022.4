# # 装饰器方式的property属性
# class Hero(object):
#     def __init__(self,name,hp):
#         self.name=name
#         self.__hp=hp
#
#     # 装饰器方式的property, 把hp方法当做属性使用, 表示当获取属性时会执行下面修饰的方法
#     @property
#     def hp(self):
#         return self.__hp
#
#     # 把hp方法当做属性使用, 表示当设置属性时会执行下面修饰的方法
#     @hp.setter
#     def hp(self, new_hp):
#         if new_hp < 0:
#             print("血量值输入非法，hp未改变")
#         else:
#             self.__hp = new_hp
#
# HanBing=Hero("寒冰",1500)
# print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))
# HanBing.hp=500
# print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))
# HanBing.hp=-500
# print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))

# 类属性方式的property属性
class Hero(object):
    def __init__(self,name,hp):
        self.name=name
        self.__hp=hp

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        if new_hp < 0:
            print("血量值输入非法，hp未改变")
        else:
            self.__hp = new_hp

    # 类属性方式的property属性
    hp=property(get_hp,set_hp)

HanBing=Hero("寒冰",1500)
print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))
HanBing.hp=500
print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))
HanBing.hp=-500
print("英雄名：%s，血量：%d"%(HanBing.name,HanBing.hp))
