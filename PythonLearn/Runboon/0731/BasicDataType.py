#  数据类型
# from numpy import outer


# Int = 100
# Float = 1.1
# Complex = 1+1j
# print(Int,Float,Complex)
#允许为多个变量赋值
# a,b,c,d = 1,"Jackyang",3.4,1+1j


# Standed Number(数字) String（字符串）List（列表） Turple（元组） Set（集合） Dictionary（字典）
# 可变数据类型 Number String Turple
# 不可变数据类型 List Set Dictionnary

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a),type(c),type(b),type(d))

# var1 = 1
# var2 = 2
# print(var1,var2)
# del var1 , var2 # 手动删除对象清空内存
# 数值运算 + - * / // % **
# str 实际上也是一个list 通过下标来截取遍历 变量[头下标；尾下标]
#   str 不可以 str变换

# list [0:-1]遍历所有list元素
# 其实需要规范输入字符 ” “ 来保证代码的可读性
# list = ['abcd',786,'jack','9999']
# tinylist = ['a','a','sd',55] 
# print(list + tinylist)

# a = [1,2,3,4,5,6,7,8,9]
# print(a)
# a[0]=9
# print(a)
# a[3:5]=[0,0]
# print(a)
# print()
#  可以利用list替换 然后

# def reverseWords(input):
#     inputWords = input.split(" ")
#     inputWords = inputWords[-1::-1]
#     # output = inputWords # 这里直接返回数组 list
#     output = ' '.join(inputWords)
#     return output

# tuple = ('abc','asdsa','jajj')
# tinytuple =('Jack')
# tuple[0]='sadasda'
# print(tuple)
# print(tuple[0])
# print(tuple[0:2])
# print(tuple[1:])
# print(tuple*2)
# print(tuple + tinytuple)


# __xxxx___ 这个属于内置 方法 不公开给你调用 可以通过 import keyword ; keyword.kwlist() to see can use functions




# if __name__ =="__main__":
#     input = "I like Mashiro"
#     rw = reverseWords(input)
#     print(rw)

# list = [1,2,3,4,4,6,7,7,8,8,99]
# print(list)
# tuple = (list)
# list[0:3]=[0,0,0]
# print(tuple)
# 可以给tuple嵌入list来修改值
'''
1.可变数据类型和不可变数据类型区别
可变数据类型：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址不发生改变，那么这个数据类型就是 可变数据类型。

不可变数据类型：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址发生了改变，那么这个数据类型就是 不可变数据类型。

总结：可变数据类型更改值后，内存地址不发生改变；不可变数据类型更改值后，内存地址发生改变。
'''

# ==============================Set========================================

# setTest = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
# if 'Baidu' in setTest:
#     print(True)

# a = set('abcdefghijklmn')
# b = set('abcdef')
# print(a,b) # 打印两个集合
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)

# for i in setTest:
#     if i == 'Google':
#         print(True)

# ========================Dictionary======================
'''字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。'''

dic = {}
# dic[Key] = value
dic['one'] = "Jack"
dic['Two'] = "Yang"
tinyDic = {"name":"Lisa","ID":123,"Birthday":1234}
print(dic)
print(dic['one'])
print(tinyDic['name'])


