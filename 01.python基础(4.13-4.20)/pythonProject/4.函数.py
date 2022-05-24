# # 公共方法
# # 1.公共方法
# # +：合并；
# # *：复制；eg：['hi']*4->['hi','hi','hi','hi']
# # print('a'*3)
# # in：判断是否在里面；not in：判断是否不在里面
# # 2.内置函数
# # len();max();min();del()
#
# # 1.函数定义
# def max(a ,b):
#     return a if a>b else b # python中的三目运算
# print(max(3,2))
# # 2.返回值
# def p(a,b):
#     sum=a+b
#     cha=a-b
#     return [sum,cha] # 可以通过列表、元组、字典返回多个数据
# result=p(1,3)
# print(result)
# # 3.缺省参数，在形参中默认有值的参数，称之为缺省参数
# # 注意：带有默认值的参数一定要位于参数列表的最后面
# def p(name,age=20): # 若不写第二个参数则默认为20，并且缺省参数只能放到最后
#     print(name,age)
# p('zhangsan')
# p('lisi',21)
# # 4.关键字参数
# def p(name,age):
#     print(name,age)
# p(age=20,name='zhangsan ')#位置参数必须在关键字参数之前
# # 5.不定长参数，当不确定参数个数时可以使用不定长参数。用包裹位置参数，或包裹关键字参数
# # （1）包裹位置参数
# # 传进的所有参数都会被args变量收集，他会根据传进参数的位置合并成一个元组，这就是包裹位置传参
# def p(*args): # 一般使用args
#     print(args)
# p('zhangsan',18) # ('zhangsan', 18)
# p('zhangsan') # ('zhangsan',)
# p() # ()
# # （2）包裹关键字传参，返回一个字典
# def p(**kwargs): # 一般使用kwargs
#     print(kwargs)
# p(name='Tom',age=2) # {'name': 'Tom', 'age': 2}
#
# # 交换两值
# a,b=1,2
# # 1.
# x=b
# b=a
# a=x
# print(a,b)
# # 2.
# a,b=b,a
# print(a,b)

# # 组包：无论是包裹位置传递还是包裹关键词传递都是一个组包的过程
# # 拆包：
# # 拆包元组数据
# def Chai():
#     return 100,200 # 返回(100,200)元组
# x1,x2=Chai()
# print(x1,x2)
# # 字典拆包,取出的是字典的key
# Dict={'name':'Zhang','age':20}
# a,b=Dict
# print(a,b) # 拆出来的是字典的key
# print(Dict[a]) # 得出value值
# print(Dict[b])

# # 引用
# # 传入不可变对象字符串，在函数内对其操作不影响调用结束后字符串的值，即不发生改变。
# # 对于可变对象，在函数体中的修改,在函数之外,该列表的内容依然发生了改变,因为python中的参数,传入的是变量引用的副本,它与变量指向同一个值.
# def test1(b):
#     b[0]+=1
# a=[1,2]
# test1(a)
# print(a) # 发生改变
# def test2(b):
#     b='abc'
# a='dd'
# test2(a)# print(a) # 未发生改变

# # 匿名函数lambda
# sum = lambda x,y:x+y
# print(sum(2,3))
#
# # 列表推导式
# list = [(x,y) for x in range(2) for y in range(3,10,2) if x<1]
# print(list)
# # [(0, 3), (0, 5), (0, 7), (0, 9)]
