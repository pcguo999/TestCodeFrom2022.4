# # 异常：当Python检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"

# # 捕获异常 try...except..
# try: # 可能产生异常的代码，放在try里
#     print('文件准备打开')
    # open('123.txt','r') # 若123.txt文件不存在则产生IOError
    # open('text.txt','r')
    # print('文件打开成功')
    # print(a) # 若a变量没有定义，那么会产生NameError异常

# # 1.捕获单个异常
# except IOError: # 若产生错误时，处理方法
# # 2.捕获多个异常
# except (IOError,NameError): # 若产生错误时，处理方法
# # 当捕获多个异常时，可以把要捕获的异常的名字，放到except 后，并使用元组的方式仅进行存储
#     pass
    # print('IOError，未找到文件')
    # 此程序看不到任何错误，因为用except 捕获到了IOError异常，并添加了处理的方法
    # pass 表示实现了相应的实现，但什么也不做；如果把pass改为print语句，那么就会输出其他信息
# # 3.存储异常信息
# except (IOError,NameError) as result: # as result存储异常的基本信息
#     print('异常为:%s'%result)
# # 4.捕获所有异常
# except Exception as result:
#    print('异常为:%s'%result)

# # else,如果没有捕获到异常,那么就执行else
# else:
#     print('没有捕获到异常')

# # try...finally...
# # 在程序中，如果一个段代码必须要执行，即无论异常是否产生都要执行，那么此时就需要使用finally。 比如文件关闭，释放锁，把数据库连接返还给连接池等
# try:
#     print('打开文件')
#     f=open('text.txt','r')
#     try:
#         print('打印a')
#         print(a)
#     except Exception as result:
#         print('异常为:%s'%result)
#     finally: # 不管是否出现异常,只要打开了文件,都需要关闭文件
#         f.close()
#         print('关闭文件')
# except Exception as result:
#     print('未找到文件')

# # 异常传递,如果try嵌套，那么如果里面的try没有捕获到这个异常，那么外面的
# # try会接收到这个异常，然后进行处理，如果外边的try依然没有捕获到，那么再进行传递。。。

# # 抛出自定义的异常
# # raise语句来引发一个异常.异常/错误对象必须有一个名字,并且它们应是Error或Exception类的子类
# class ShortInputError(Exception):
#     def __init__(self,length,least):
#         self.length=length
#         self.least=least # 最短长
# def main():
#         try:
#             s=input('please input:')
#             if len(s)<3: # raise引发一个自己定义的异常
#                 raise ShortInputError(len(s),3)
#         except ShortInputError as result:
#             print('ShortInputError:输入的长度是%d,长度至少应该是%d'%(result.length,result.least))
#         else:
#             print('Not Error!')
# main()
