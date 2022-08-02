# 集合(set)是一个无序的不重复的元素序列
# 可以使用大括号{}或者set() 函数来创建集合，注意：创建一个空集合必须使用set（），空集合不能用set（）
# setNums={value1,value2,....}
# set(value)
# basket = {'apple', 1, 2, 3, 4, 5, 'orange'}
# print(basket)
# print('apple' in basket)
# a = set('abracabdabra')
# b = set('alacazam')
# print(a,b)
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)
# # 可以用集合的概念来理解 交 并 补

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
