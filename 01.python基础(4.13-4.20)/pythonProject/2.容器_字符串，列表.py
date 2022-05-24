# 字符串-》''，“”，‘’‘ ’‘’，“”“ ”“”
# 列表-》[]
# 元组-》()
# 字典-》{}

# # 一、字符串
# name='郭鹏程'
# f_name=f'这是{name}的操作'
#   # 单引号或者双引号或者三引号中的数据，就是字符串
# print("%s" % name)
# print(f_name)#f-strings输出
# UserName=input('请输入用户名：')
# PassWord=input('请输入密码：')
# print('用户名：%s' % UserName)
# print('密码：%s' % PassWord)
#
# # 1.下标和切片
# name='abcdef'
# print(name[1])#使用下标
# print(name[2])
# print(name[3])
# print(name[0:2])#ab，不包括下标为2
# print(name[::-1])#取反，从最后一个开始，每次向前
# print(name[1:5:2])#bd,从下标为2开始到4，每次跳过1个
#     # 切片的语法：[起始:结束:步长]
#     # 注意：选取的区间从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)，步长表示选取间隔
#
# # 2.字符串常见操作
# # find查找操作，成功返回索引值，否则返回-1
# # rfind,类似find，只不过是从右边开始查找
# name='Jack is a boy'
# fname='ck'
# i=name.find(fname)
# i=name.find('z')
# print(i)
# # index和find一样，但是若是不在里面会报错
# # rindex和index一样，只不过是从右边开始
# i=name.index('a')
# i=name.index('z')
# print(i)
# # count返回从开始到结束出现的次数mystr.count(str, start=0, end=len(mystr))
# i=name.count(fname)
# print(i)
# # replace，将str1替换成str2 替换，可以设置替换次数
# name2=name.replace("a","x",1)   #注意：并不会改变原来的name
# # split分隔符切片，以str为分界，分成i组
# name2=name.split(" ",2)#以空格分开，分两次
# # splitlines按行分隔，返回一个包含各行作为元素的列表
# name='I am a boy\n My name is GuoPengCheng'
# name2=name.splitlines()
# # capitalize把第一个字符大写
# name='abce'
# name2=name.capitalize()
# # title将每个单词的首字母大写
# name2=name.title()
# # startswith检查字符串是否以str开头，是则返回真，否则返回假
# name2=name.startswith('J')
# # endswith查看是否是以str结尾
# name2=name.endswith('y')
# # lower将所有大写改成小写
# name2=name.lower()
# # upper将所有小写改成大写
# name2=name.upper()
# # lstrip删除字符串左边的空白字符
# name='  I am a boy   '
# name2=name.lstrip()
# # rstrip删除字符串右边的空白字符
# name2=name.rstrip()
# # strip删除字符串两边的空白字符
# name2=name.strip()
# #partition将字符串以str分割成三部分，str前，str和str后
# name2=name.partition("am")
# #rpartition和partition一样，只不过是从右边开始
# # isalpha若字符串所有字符都是字母则返回真
# name2=name.isalpha()
# # isdigit若字符串所有字符都是字母或数字则返回真
# name='123abc'
# name2=name.isdigit()
# # isalnum若字符串所有字符都是字母或数字则返回真
# name='123abc'
# name2=name.isalnum()
# # isspace若字符串只包含空格，返回真
# name='  '
# name2=name.isspace()
# print(name)
# print(name2)
# # join，str字符串中每个元素后面拼接上对象字符串，构造一个新字符串
# str=' '
# li=['my','name','is','Guo']
# str2=str.join(li) # 注意是将对象放到参数中
# print(li)
# print(str2)
#
# # 二、列表
# # 比c语言强大之处在于列表元素可以是不同类型的！！！
# list=[1,'a']
# print(list)
# print(list[1])
# # 1.列表循环遍历
# list=['ZhangSan','WangWu','ZhaoSi']
# for name in list:
#     print(name)
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1
# # 2.列表的相关操作
# # （1）添加元素：append,extend,insert
# #   append：添加到列表后
# A=['A','B','C']
# x=input('请输入要添加的学生姓名：')
# A.append(x)
# print('添加后：')
# for i in A: # 单独打印
#     print(i)
# print(A)
# #   extend：将另一个集合中的元素逐一添加到列表中
# B=['a','b','c']
# A.append(B) # ['A', 'B', 'C', ['a', 'b', 'c']]
# A.extend(B) # ['A', 'B', 'C', 'a', 'b', 'c']
# #   insert(index, object) 在指定位置index前插入元素object
# A.insert(2,'OK')
# print(A)
# # （2）修改元素，直接用下标修改
# A[1]=2
# print(A)
# # （3）查找元素：in,not in,index,count
# # in：若存在则返回真，not in若不存在则返回真
# x=input()
# if x in A:
#     print('查找到')
# else:
#     print('未找到')
# # index找到则返回下标，否则报错
# print(A.index(x))
# print(A.index(x,0,1))
# # count查找出现次数
# print(A.count('C'))
# # （4）删除元素：del,pop,remove
# # del：根据下标进行删除
# # pop：删除最后一个元素，类似出栈
# # remove：根据元素的值进行删除
# del A[1]
# A.pop()
# A.remove('B')
# print(A)
# # （5）排序：sort,reverse
# A=['B','A','C']
# A.sort()
# A.reverse()
# print(A)
# # 3.列表嵌套
# 一个学校有三个办公室，现有8个老师等待分配，请编写程序，实现随机分配
# import random
# offices=[[],[],[]]
# Teachers=['A','B','C','D','E','F','G','H']
# for name in Teachers:
#     i=random.randint(0,2)
#     offices[i].append(name)
# print(offices)