# def foo(arg, a):
#   x = 100
#   y = 'hello python!'
#   for i in range(10):
#     j = 1
#     k = i
#   def b(a):
#       print(locals())
#   b(a)
#   print(locals())
# foo(1, 2)
# print(locals())



# class A:
#     def __init__(self):
#         self.name = 'zhangjing'
#     def method(self,a):
#         print("method print")
# Instance = A()
# t=A()
# print(t.__delattr__('name'))
# print(hasattr(t, "name"))   #判断属性是否存在
# print(setattr(t, "age", "18"))   #为属相赋值，并没有返回值
# print(hasattr(t, "age") )   #属性存在了
# print(delattr(t, "age"))   #为属相赋值，并没有返回值
# print(hasattr(t, "age") )
# len('ssdd')
# 'ssdd'.__len__()
# print (getattr(Instance , 'name', 'not find'))
# print (getattr(Instance , 'age', 'not find') )  #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'
# print (getattr(Instance, 'method', 'default'))
# getattr(Instance, 'method', 'default')(1)
# t=A()
# print(hasattr(t, "name")) #判断对象有name属性
#
# print(hasattr(t, "method"))  #判断对象有run方法





# class Shape:
#   def __dir__(self):
#     return ['area','perimeter','location']
#   def __len__(self):
#     return 1
# s=Shape()
# print(dir(s))
#
# a='abcd'
# # print(a.__len__())
# # print(len(s))
#
# print(dir())
# print(locals())

# class test():
#       name="xiaohua"
#       def __init__(self):
#         self.__name='zhangsan'
#       def run(self):
#         return "HelloWord"
# t=test()
# t1=test()
# test.name='lisi'
# #print(test.name)
# print(t.name+'%%%'+t1.name+'%%%'+test.name)
# #print(t.name)

# from sys import *
# #print(globals())
# __name__='1'
# a=dict(globals())
# print(len(a))
# if __name__ == '__main__':
#   for i,j in a.items():
#     print(i,j)



# a='abcdefg'
# class B():
#     def __init__(self):
#       self.a=1
#       self.x='656'
#     def suiyi(self):
#       self.d=2
#     c='djfj'
# b=B()
# b.suiyi()
# del b
# del B
#
# print(dir())
# print(vars())
# print(len(dir()))
# print(len(vars()))
# #print(dir()[1:5])
# print(dir(B))
# #print(dir(b))
# print(vars(B))
# #print(vars(b))

# import json
# a=[{1:'a',2:'b',3:'c',4:'d'}]
# jsons=json.dumps(a)
# print(jsons)
# print(type(jsons))
# obj=json.loads(jsons)
# print(obj)
# print(type(obj))


#2.44


#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# s =Student()
# s.score = 9999
#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
# s = Student()
#s.set_score(60) # ok!
# print(s.get_score())
# # 60
# print(s.set_score(9999))
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!


# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# #@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
# s = Student()
# s.score = 60 # OK，实际转化为s.set_score(60)
# print(s.score) # OK，实际转化为s.get_score()
# # 60
# s.score = 9999
# #Traceback (most recent call last):
# #   ...
# # ValueError: score must between 0 ~ 100!
# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2018 - self._birth
#
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


# for i in range(10,0,-2):
#   print(i)

# myslice=slice(5)
# print(myslice)

# s=slice(0,2,1)
# a=[1,2,3,4,5,6,7,8,9]
# print(a[s])

