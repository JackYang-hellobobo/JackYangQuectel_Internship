'''
以下为Runoob的Python3实例练习
此作为记录说明 每一个实例均以函数封装好供测试验证
'''
import math
import random


def example1():
	print("hello World !")


def example2():
	x, y = eval(input("请键入需要求和的两个数字："))
	print(x + y)


def example3():
	x = int(input())
	y = math.sqrt(x)
	print(y)


def example4():
	# a^2*x+b*x+c=y
	a, b, c = eval(input("Please enter 3 args :"))  # 多个参数键入
	# print(a, b, c)
	beta = b * b - 4 * a * c
	if beta >= 0:
		x1 = (- b - beta) / (2 * a)
		x2 = (-b + beta) / (2 * a)
		print(x1, x2)
	else:
		print("没有实数根")


def example5():
	a, b, c = eval(input("Please enter 3 args :"))  # 多个参数键入

	s = float((a + b + c) / 2)
	area = (s * (s - float(a)) * (s - float(b))(s - float(c))) ** 0.5
	print(area)


def example6():
	r = eval(input("Enter R:"))
	area = 2 * math.pi * r
	print(area)


def example7():
	random_number = random.randint(1, 9)  # 取头不取尾 ????? 我感觉我智商被摁在地上反复摩擦
	# random.randint(a,b)
	# 函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。
	print(random_number)


if __name__ == "__main__":
	# example1()
# example2()
	# example3()
	# example4()
	# example5() TypeError: 'float' object is not callable
	# example6()
	# example7()
	exit()
