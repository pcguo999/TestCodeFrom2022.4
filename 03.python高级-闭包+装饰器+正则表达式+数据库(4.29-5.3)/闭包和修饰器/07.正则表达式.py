# 导入re模块
import re
# # 使用match方法匹配数据
# a=re.match('abc','abcd')
# # 提取数据
# print(a.group())
# {m,n}匹配前一个字符出现从m到n次
# $匹配字符串结尾
# a = re.match("[a-zA-Z0-9_]{4,20}@(qq|163|sina).com","abcd@qq.com")
# print(a.group())

# (?P<name>)分组起别名
# (?P=name)引用别名为name分组匹配到的字符串
a = re.match("(aa)(bb).\\2\\1","aabb.bbaa")
print(a.group())
# aabb.bbaa