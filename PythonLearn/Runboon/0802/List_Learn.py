# list1 = ['Google', 'Runoob', 1997, 2000]
# list2 = [1, 2, 3, 4, 5]
# list3 = ["a", "b", "c", "d"]
# list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list1[0], list1[1], list1[2])
# print(list4[-1], list4[-2], list4[-3], list4[-4])
# print(list5[-1:1])  # 默认的方向还是从左到右边 一定需要遵循顺序来切片列表
#
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.append('Baidu')  # 尾部连接
# print("更新后的列表 : ", list1)
# list1.pop()  # 尾部抛出
# print("更新后的列表 : ", list1)
# # 也可以通过del命令来对列表删除指定索引的元素
# del list1[0]
# print(list1, len(list1), list1 + list1, list1 * 2, 'Google' in list1)
#
# for x in list1:
# 	print("type:{},value:{}".format(type(x), x)) #格式化代码真好用

#  怎么让两个数字数组相加呢？
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [6, 7, 8, 9, 10]
# print(nums2+nums1) # 这里的+号 仅用到字符串拼接功能
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = [a, b]
# for x in c:
# 	print("type:{},value:{}".format(type(x), x))
# 	for y in x:
# 		print("type:{},value:{}".format(type(y), y))
#
# # 确实可以通过这样子嵌套解包
# L = ['Google', 'Runboob', 'Taobao']
#
# import  operator
#
# a = [1, 2]
# b = [1, 2]
# c = [2, 3]
# print("operator.eq(a,b)", operator.eq(a, b))
# print("operator.eq(a,b)", operator.eq(a, c))
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = (1, 2, 3, 4, 5)
# list3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(list3.count(1)) # 统计某个元素在列表中出现的次数
# print(list3.index(1)) # 括号里面是参数你要查找到元素，函数返回的是第一个元素的下标
# print(list1, len(list1), max(list1), min(list1), list(list2))
#
# list1.reverse()#列表反转
# print(list1)
# list1.sort() #将列表从小达到排列了一遍
# print(list1)
# list_copy = list1.copy()
# print(list_copy)
# list_copy.clear()
# print(list_copy)
#
