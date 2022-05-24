# # 一、元组-》()
# # 元组不能修改
# # 1.输出
# Tuple=('a',1,2,1)
# print(Tuple[0])
# print(Tuple)
# # 2.查找：count，index
# print(Tuple.count(1))
# print(Tuple.index(2))

# # 二、字典-》{}
#
# # 常见操作
# # 1.查看元素
# # 通过key和使用get方法来查找
# # get方法查找某个键，还可以设置默认值
# info = {'name': '郭鹏程', 'gender': 'man', 'id': 1}
# print(info)
# print(info.get('age', 18))  # 若找不到则返回默认值18
# print(info['name']) # 通过key键查看
# # 2.修改
# newname=input('请输入新的学号：')
# info['id']=int(newname)
# print(info)
# # 3.添加
# # （1）添加新键，使用变量名[‘键’]=数据的时候若‘键’不存在则会新增这个元素
# age=input('请输入年纪：')
# info['age']=int(age)
# print(info)
# # （2）
# # 4.删除：del，clear
# # del删除指定元素
# del info['age']
# print(info)
# # clear删除整个字典
# info.clear()
# print(info)
# # 5.len查找键值对个数
# print(len(info))
# # 6.keys返回一个包含所有键的列表
# print(info.keys())
# # 7.values返回一个包含所有值的表
# print(info.values())
# # 8.items返回一个包含所有（键，值）元组的列表
# print(info.items())
# # 9.遍历字典
# for i in info.keys(): # 通过key遍历
#     print(i)
# for i in info.values(): # 通过value遍历
#     print(i)
# for i in info.items(): # 通过item遍历项
#     print(i)
# for key,value in info.items(): # 通过item遍历键值对
#     print('key=%s,value=%s'%(key,value))
# # 10.有序字典，字典是无序的，若想有序输出，则使用OrderedDict()

# #  set集合和字典类似，是{}
# a = [1,2,3]
# print(set(a))
# print(tuple(a))