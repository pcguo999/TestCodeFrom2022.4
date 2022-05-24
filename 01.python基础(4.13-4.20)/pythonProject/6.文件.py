# f=open('text.txt','r')
# print(f.read(2)) # 读两个数据，若没有参数表示全读
# print(f.readlines()) # 类似read无参,但这时因为指针已经过了两个，所以从第三个开始读
# print(f.readline()) # 只读一行
# f.close()

# # 制作文件副本
# name=input('请输入文件名称（加上文件类型）')
# # 以读的方式打开文件
# file=open(name,'rb')
# flagnum=name.rfind('.')
# if flagnum>0:# 若找到'.'所在位置
#     flag=name[flagnum:] # 找文件后缀
# # 组织新名字
# newname=name[:flagnum]+'[复件]'+flag
# # 创建新文件
# newfile=open(newname,'wb')
# newfile.writelines(file.readlines())
# file.close()
# newfile.close()


# import os
# # 文件重命名
# os.rename('text.txt','text_最终.txt')
# # 删除文件
# os.remove('text[复件].txt')
# # 创建文件夹
# os.mkdir('GPC')
# # 获取当前目录
# print(os.getcwd()) #C:\Users\24708\PycharmProjects\pythonProject
# # 改变默认目录
# os.chdir('../')
# print(os.getcwd()) #C:\Users\24708\PycharmProjects
# # 获取目录列表
# print(os.listdir())
# #  删除文件夹
# os.rmdir('GPC')

# # 批量修改文件名
# import os
# flag=1 # 1表示添加标准，2表示删除
# # os.mkdir('rename')
# foldername='rename/'
# # 获取指定路径的所有文件名字
# dirList=os.listdir(foldername)
# # 遍历输出所有文件名字
# for name in dirList:
#     print(name)
#
#     if flag==1:
#         newname='[GPC]-'+name
#     elif flag==2:
#         num=len('[GPC]-')
#         newname=name[num:]
#     print(newname)
#     # 因为是在文件夹里面，所以文件名称要加上路径
#     os.rename(foldername+name,foldername+newname)