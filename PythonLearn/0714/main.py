# def caclulate(x,y):#需要重点学习python的语法 数据类型以及vscode debug功能
#     z=x+y
#     return z


# def main():
#     x=int(input())#需要注意的是input录入对象的属性是字符串str类型
#     y=int(input())
#     print(caclulate(x,y))

# main()
# from regex import X


# def myfunc():
#     global  x #声明了全局变量后 你可以在函数外对面global var进行操作赋值
#     x = "fantastic"
#     print(x)

# myfunc()#需要执行一遍函数过后才能变量声明
# x="Test Global or local"
# print(x)
# print(type(x))

# x=1 #int
# y=1.1#float
# z=1j#complex
# #to verify the type of any object in python  use the type() function

#数据类型演示 int float complex
# x = 35e3
# print(x)
# print(type(x))
# y=3+5j
# print(y)
# print(type(y))
# '''
# 其实这个也不是标准的注释类型 在python里面只有官方认定的标准注释就行#
# '''
# import random #Random module.

# print(random.randrange(1, 10))#取头不取尾部 即改函数的目的就是 在1-9之间取得一个数

from matplotlib.pyplot import pink

# "in" and " not in" 使用方法
txt = "The best things in life are free!"
if "free" in txt:
    print(True)
else:
    print(False)
if "jackyang"   not in txt:
    print(True)
else:
    print(False)    