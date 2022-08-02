# print("Hello World")
'''
python --verrsion

python enter in REPL

# python xxxx.py  to introduce the .py files 

'''

# 多行语句可以用\切换
# total = 1 + \
#     2 + \
#     3
# print(total)

# Python里面只有4种数据类型 整型 布尔型 浮点型 复数
# int()
# float()
# bool()
# complex()

# Python 字符串类型String
'' '' ''
# '''''' 可以指定一个多行字符串
# \ 转义
# 反斜杠可以用来转义，可以使用r参数可以让反斜杠不发生转义。如 r"this is a line with \n" \n会显示，并不是换行。
# 字符串可以用 ”+“ 运算符链接在一起 用”*“ 运算符重复
#  Python 字符串有两种索引方式，从左到右以0开始，从右边往左以-1开始
#  Python中的字符串不能改变
# Python没有单独的字符串类型 一个字符就是长度为1的字符串
# 字符串的截取的语法格式如下 ： 变量[头下标：尾下标：步长]  str.split ?

str = "123456789"
print(str)
print(type(str))
print(str[0:-1])#取头不取尾
print(str[0])#取字符串的开头
print(str[3:5])#get str 4th 2 6th char
print(str[2:])#get str 3th to last one
print(str[1:5:1])#get 2th to 6th step by 1
print(str*2)# print str 2
print('--------------------------------')#print str
print(str+"你好")

print('hello\nworld')#test \ \n
print(r"hello World \n test") # r 即 raw string 原始字符串 注意和row的区别 这个是一排的意思

# Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
import sys

# from sympy import print_rcode;x="jackyang";sys.stdout.write(x+"\n")

print() #print 默认输出是换行的 如果要实现不换行 需要在变量末尾加上 end =" ":

def main():
    a = 'x'
    b = 'y'
    print(a)
    print(b)
    print('------------------')
    print(a,end="")
    print(b,end="")
    print()

main()

