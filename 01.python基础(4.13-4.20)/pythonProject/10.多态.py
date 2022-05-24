# # 什么是多态?
# # 在需要使用父类对象的地方,也可以使用子类对象, 这种情况就叫多态.
# # 比如, 在函数中,我需要调用 某一个父类对象的方法, 那么我们也可以在这个地方调用子类对象的方法.
# # 如何在程序中使用多态?
# # 可以按照以下几个步骤来写代码:
# #     1.子类继承父类
# #     2.子类重写父类中的方法
# #     3.通过对象调用这个方法
# class father(object):
#     def cure(self):
#         print('父亲给病人治病')
# class son(father):
#     def cure(self):
#         print('儿子给病人治病')
# # 定义函数，在里面调用医生的cure函数
# def call_cure(doctor):
#     doctor.cure()
# f=father()
# call_cure(f)
# s=son()
# call_cure(s)
# # 给call_cure(doctor)函数传递哪个对象,在它里面就会调用哪个对象的cure()方法,
# # 也就是说在它里面既可以调用son对象的cure()方法,也能调用father对象的cure()方
# # 法,当然了也可以在它里面调用Father类其它子类对象的cure()方法,这样可以让
# # call_cure(doctor)函数变得更加灵活,额外增加了它的功能,提高了它的扩展性.