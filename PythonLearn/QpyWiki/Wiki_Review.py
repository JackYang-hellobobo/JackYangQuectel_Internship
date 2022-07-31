# # def append_element(some_list,element):
# # 	some_list.append(element)
# #
# # data = [1,2,3,4]
# # append_element(data,5)
# # print(data)
#
# def func(a):
# 	return isinstance(a, (int, float, str, complex))  # 这个is instance来是否属于某种类型
#
#
# print(func(2.4))
#
#
# # 可以检查对象的类型是否在元组中：
#
# def isiterable(obj):
# 	try:
# 		iter(obj)
# 		return True
# 	except Exception as e:
# 		return False
#
#
# # 不可变数据类型 Number String Tuple
# # 可变数据类型 List Dictionary Set
# a = [1, 2, 3, 4, 5, 6]
# print(isiterable(a))
# print(isiterable('a string'))
# print(isiterable(5))
# print(id(a))
#
# # 1.可变数据类型和不可变数据类型区别
# # 可变数据类型：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址不发生改变，那么这个数据类型就是 可变数据类型。
# #
# # 不可变数据类型：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址发生了改变，那么这个数据类型就是 不可变数据类型。
# #
# # 总结：可变数据类型更改值后，内存地址不发生改变；不可变数据类型更改值后，内存地址发生改变。
#
# a = "one way of writing a string"
# b = "another way"
# '''jackayng
# 	这样子声明子字符串其实是不太好的 可能会增加.py size 和
# '''
# import math
#
# x = -10
# print(x)
# print(abs(x))
# print(math.exp(2))
# print(math.fabs(-10.2))
# print(math.log10(100))
# print(math.pi)
# print(math.pow(2, 4))
#
# import random
#
# print(random.choices(range(0, 10)))# 取头不取尾部
# print(random.random()) #随机生成一个【0，1）的数
# print(random.uniform(0,10)) #指定范围内将序列所有元素随机排序

'''
之所以使用python也是因为它对字符串处理的高效性
实习工作处理还是对我技能学习的提升还是蛮有帮助的
'''
# var1 = 'HelloPython'
# var2 = 'QuectelP\a' \
#        '\n' \
#        '\\' \
#        '\'' \
#        '' \
# 'ython'
# print(var1[:-1])  # 取头不取尾部
# print(var1[0:len(var1) - 5])


# + * [] [:] in not in r/R 字符串运算符号
# print(r'\n')
# print(R'\n')
# print('My name is JackYang%s,age is %d' % ('helloboo', 21))
# print('My name is JackYang{},age is {}'.format('helloboo', 21))

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print(list1)
# # access list just like Java or C ++ of the Array
# print(list4[0], list4[4], list4[3], list4[2], list4[1])
# # String also could reverse to access
# print(list4[-1])
# print(list4[-2])
# print(list4[-3])
# print(list4[0:4]) # 输出的还是列表
# print(list4)
# list4.append('puple')
# print(list4)
# list4.pop(-1)
# del list4[-1]
# print(list4)
# var1 = [1, 2, 3]
# var2 = [4, 5, 6]
# print(var2 + var1)  # list 拼接
# print(len(var2 + var1))
# print(3 in [1, 2, 3])
# for x in var2:
# 	print(x, end=" ") # 默认print 后面会补充\n换行符号  通过end = ""可以通过取消\n 而且还能自定义结尾的字符串
# # 字符串的截取和拼接
# L = ['Google', 'Runoob', 'Taobao']
# print(L[2])
# print(L[-1])
# print(L[-2])
# print(L[1:-1])
#
# squares = [1,2,3,4,4,5,,5,,6,,6,7,]
# array = [1, 2, 3, 4, 5, 6]
# array += array
# print(array)  # 这个仅仅是对list的拼接而已啊
#  嵌套列表的意思有点想二维数组 其实对于程序来说 键盘真的很重要就像老婆一样 爱她 天天敲她
a = [1, 1, 1, 1, 1]
b = [1, 2, 3, 4, 5]
c = (12,3,4,5)
x = [a, b]
print(b)
b.reverse() # didn't hava return value
print(b)
print(a.count(1))
print(b.index(2))
print(x)
print(len(x)) # 元组可以转换成列表
print(c)
c = list(c)
print(c)
print(max(a,b))
# print(x[0][1])  # 选表选参数
