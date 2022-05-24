__all__=["add1","min"]
def add1(a,b):
    return a+b
def min(a,b):
    return a if a<b else b
# 用来进行测试:但是其他文件引用该文件时这一部分也会运行
# 为了不让其他文件引用时运行,使用变量__name__
# ret=add(1,2)
# print(ret)
# print("in test.py file,__name__is %s"%__name__)
# 根据__name__变量可以判断出是否是在该文件中被运行
if __name__=='__main__':
    # 若运行的是该文件,则__name__==__main__
    # 若运行的不是该文件,只是引用该文件,则__name__==test
    ret=add1(1,2)
    print(ret)