# 键必须唯一，但是值不必

# tinydir = {'name':'Jack',1:'Yang','name3':'hellobobo'}
# print(tinydir)
# print(len(tinydir),type(tinydir))
# print(tinydir['name']+tinydir[1]+tinydir['name3'])
#
# tinydir['name']='Lisa' # 成功修改了键值
# print(tinydir)
# del tinydir['name3']
# print(tinydir)
# tinydir.clear()
# print(tinydir)
# del tinydir
# print(tinydir) # 已经被删除现在内存

# 可变和不可变 是针对值改变了 地址是否改变的 如果内存地址不改变 则为可变数据类型 如果跟着改变则为不可变类型

# 可变数据类型 num str tuple
# 不可变数据类型 list dic set

# tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'} # 字典里不允许同一个键出现两次，创建时间如果同一个键被赋值两次，后一个值会被基础（理解也就是前一个键值会被覆盖）
#
# print(tinydict.get('Name'))

# dict1 = {"Name": 'Jack', 'Name1': 'Yang', "Name2": "Hellobobo"}
# dict2 = {"Name": 'Li', 'Name1': 'cui', "Name2": "Ting", "Name3": "TestFunctions"}
# print(dict1)
# dict1.update(dict2)
# print(dict1)

# sl = {1,2,3,4,4,5,6,7,8}
# print(sl)
# sl.add('Google')
# print(sl)

tinySet = set(('Google', 'Java', 'Kotlin'))  # 会将元组解包存入为集合元素
print(tinySet)
tinySet.update(['AZ', 'WS'])
print(tinySet)
# tinySet.remove('Jack') # 如果没有此element 则会报错
print(tinySet)
tinySet.discard('JackYang')
print(tinySet)
print(len(tinySet))
tinySet.clear()
print(tinySet)
print("Jack" in tinySet)
# tinySet.pop()
# print(tinySet) #集合这样子抛元素是不稳定的



