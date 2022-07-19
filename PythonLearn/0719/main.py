
'''
Date: 2022/7/19 Tuesday Sunny
Author : JackYang
'''
class Student(object):
    '''定义一个学生类来理解Python面向对象编程的思想'''    
    def __init__(self) -> None: #所以定义类方法的时候需要对类对象self传入类方法中进行管理 类似于c++的this
        self.name = " "
        self.sex = " "
        self.id = ""
    
    def setStuID(self,newid):
        self.id = newid
    
    def getStuID(self):
        return self.id

    def setName(self,newname):
        self.name = newname
    
    def getName(self):
        return self.name
    
    def setSex(self,newSex):
        self.sex = newSex
    
    def getSex(self):
        return self.sex

stu_yang = Student()
stu_yang.setName("JackYangHellobobo")
stu_yang.setStuID("201912700003")
stu_yang.setSex("Male")
# 其实这样有点不符合Python简洁至上的功能 代码行数冗余还不利于维护 写长不要紧 但是不能冗余 要是参数多了 你这样一个方法一个方法的写来传递 “复杂”
print(stu_yang.getName())
print(stu_yang.getSex())
print(stu_yang.getStuID())



    