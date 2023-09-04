# class Demo:
# 	__x = 0
# 	def __init__(self, i):
# 		self.i = i
# 		Demo.__x += 1

# 	def hello(self):
# 		print("hello", self.i)
# a = Demo("Tom")

# print(a.hello(self))

# class Demo:
# 	i=0   #i 類別變數
# 	def __init__(self,i):
# 		self.i = i  #i 實體變數
# 		Demo.i += 1
# 	def hello(self):
# 		print("hello",self.i)

		
# print("There are", Demo.i, "instances.")
# a = Demo(1122)
# a.hello()
# print("a.i =", a.i)
# b = Demo(3344)
# b.hello()
# print("b.i =", b.i)
# c = Demo(5566)
# c.hello()
# print("c.i =", c.i)
# d = Demo(7788)
# d.hello()
# print("d.i =", d.i)
# e = Demo(9900)
# e.hello()
# print("e.i =", e.i)
# '''
# print("a.i =", a.i)
# print("b.i =", b.i)
# print("c.i =", c.i)
# print("d.i =", d.i)
# '''

# print("After all, there are", Demo.i, "instances.")

# class Demo:
# 	__x = 0
# 	def __init__(self, i):
# 		self.__i = i
# 		Demo.__x += 1
# 	def hello(self):
# 		print("hello", self.__i)
# 	@classmethod
# 	def getX(cls):
# 		return cls.__x

# a = Demo('Tom')
# print(Demo.getX())

class Demo:
	__x = 0
	def __init__(self, i):
		self.__i = i
		Demo.__x += 1
	def hello(self):
		print("hello", self.__i)
	@classmethod
	def getX(cls):
		return cls.__x
	@classmethod
	def add(cls):
		Demo.__x +=1
class subDemo(Demo):
	pass
a = Demo("Tom")
b = subDemo("John")
#isinstance
print(isinstance(a, Demo))
print(isinstance(a, subDemo))
print(isinstance(b, Demo))
print(isinstance(b, subDemo))
#issubclass
print(issubclass(subDemo, Demo))
print(issubclass(Demo, subDemo))