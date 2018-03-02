'''
1,111
delattr（object，name ）
delattr是删除属性
del是删除引用
但是在下面的情况它们都是一样的
比如有一个对象x,它有个属性为foo,则下面的代码是等价的
delattr(x, "foo")等价于del x.foo
这是一个相对的setattr()。参数是一个对象和一个字符串。该字符串必须是对象属性之一的名称。该函数删除指定的属性，只要该对象允许。例如，相当于。delattr(x, 'foobar')del x.foobar

班dict（** kwarg ）
类dict（映射，** kwarg ）
类dict（可迭代，** kwarg ）
创建一个新的字典。该dict对象是字典类。请参阅dict和映射类型 -有关此类文档的字典。

对于其他容器看到内置list，set以及 tuple类，还有collections模块。

dir（[ object ] ）
没有参数，返回当前本地作用域中的名称列表。使用参数尝试返回该对象的有效属性列表。

如果该对象具有一个名为的方法__dir__()，则此方法将被调用，并且必须返回属性列表。这允许实现自定义__getattr__()或__getattribute__()功能的对象 定制dir()报告其属性的方式 。

如果对象没有提供__dir__()，那么函数尽量从对象的__dict__属性（如果已定义）以及从其类型对象收集信息。结果列表不一定完整，并且在对象具有自定义时可能不准确__getattr__()。

默认dir()机制的行为与不同类型的对象有所不同，因为它试图产生最相关的信息，而不是完整的信息：

如果对象是模块对象，则列表将包含模块属性的名称。
如果对象是类型或类对象，则列表包含其属性的名称，并递归地显示其基础的属性。
否则，该列表包含对象的属性名称，其类属性的名称以及其类的基类的属性的递归。
结果列表按字母顺序排序。例如：

>>>
>>> import  struct
>>> dir （）   ＃显示模块名称空间中的名称
['__builtins__'，'__name__'，'struct']
>>> dir （struct ）   ＃显示struct module中的名称
['Struct '
__all__'，__builtins__，__cached__，__doc__，
__file__，__initializing
__，__loader__，__name__，__package__，_clearcache，calcsize，error， 'pack'，'pack_into'，'unpack'，'unpack_from']
>>> class  Shape ：
...    def  __dir__ （self ）：
...         return  [ 'area' , 'perimeter' , 'location' ]
>>> s  =  Shape （）
>>> dir （s ）
['area'，'location'，'perimeter']
注意 由于dir()主要是为了方便在交互提示中使用，因此它试图提供一组有趣的名称，而不是试图提供严格或一致定义的名称集，而且其详细行为可能会在不同版本之间发生变化。例如，当参数是一个类时，元类属性不在结果列表中。

getattr()函数是Python自省的核心函数，具体使用大体如下：

获取对象引用getattr
Getattr用于返回一个对象属性，或者方法

Python代码
getattr()
class A:
    def __init__(self):
        self.name = 'zhangjing'
    def method(self):
        print("method print")
Instance = A()
print (getattr(Instance , 'name', 'not find'))
print (getattr(Instance , 'age', 'not find') )  #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'
print (getattr('a', 'method', 'default'))
#如果有方法method，否则打印其地址，否则打印default
print getattr(a, 'method', 'default')()
#如果有方法method，运行函数并打印None否则打印default

注：使用getattr可以轻松实现工厂模式。
例：一个模块支持html、text、xml等格式的打印，根据传入的formate参数的不同，调用不同的函数实现几种格式的输出



Python代码
import statsout
def output(data, format="text"):
     output_function = getattr(statsout, "output_%s" % format)
    return output_function(data)


setattr(	object, name, value)
This is the counterpart of getattr(). The arguments
are an object, a string and an arbitrary value. The string may name an existing
attribute or a new attribute. The function assigns the value to the attribute,
provided the object allows it. For example, setattr(x,
'foobar', 123) is equivalent to
x.foobar = 123.

 这是相对应的getattr()。参数是一个对象,一个字符串和一个任意值。字符串可能会列出一个现有的属性或一个新的属性。这个函数将值赋给属性的。该对象允许它提供。例如,setattr(x,“foobar”,123)相当于x.foobar = 123。

delattr(	 	 	 	object, name)
This is a relative of setattr(). The arguments are
an object and a string. The string must be the name of one of the object’s
attributes. The function deletes the named attribute, provided the object allows
it. For example, delattr(x, 'foobar') is
equivalent to del x.foobar.

与setattr()相关的一组函数。参数是由一个对象(记住python中一切皆是对象)和一个字符串组成的。string参数必须是对象属性名之一。该函数删除该obj的一个由string指定的属性。delattr(x, 'foobar')=del x.foobar





hasattr用于确定一个对象是否具有某个属性。

语法：
 hasattr(object, name) -> bool
判断object中是否有name属性，返回一个布尔值。
>>> li=["zhangjing","zhangwei"]

>>> getattr(li,"pop")
<built-in method pop of list object at 0x011DF6C0>
>>> li.pop
<built-in method pop of list object at 0x011DF6C0>

>>> li.pop()
'zhangwei'

>>> getattr(li,"pop")()
'zhangjing'

>>>getattr(li, "append")("Moe")

2.2222
hasattr(object, name)
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
需要注意的是name要用括号括起来

复制代码
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> hasattr(t, "name") #判断对象有name属性
 8 True
 9 >>> hasattr(t, "run")  #判断对象有run方法
10 True
11 >>>

3.33333
getattr(object, name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。

复制代码
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> getattr(t, "name") #获取name属性，存在就打印出来。
 8 'xiaohua'
 9 >>> getattr(t, "run")  #获取run方法，存在就打印出方法的内存地址。
10 <bound method test.run of <__main__.test instance at 0x0269C878>>
11 >>> getattr(t, "run")()  #获取run方法，后面加括号可以将这个方法运行。
12 'HelloWord'
13 >>> getattr(t, "age")  #获取一个不存在的属性。
14 Traceback (most recent call last):
15   File "<stdin>", line 1, in <module>
16 AttributeError: test instance has no attribute 'age'
17 >>> getattr(t, "age","18")  #若属性不存在，返回一个默认值。
18 '18'
19 >>>

44.44
setattr(object, name, values)
给对象的属性赋值，若属性不存在，先创建再赋值。

复制代码
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> hasattr(t, "age")   #判断属性是否存在
 8 False
 9 >>> setattr(t, "age", "18")   #为属相赋值，并没有返回值
10 >>> hasattr(t, "age")    #属性存在了
11 True
12 >>>

5.5555555class property（fget = None，fset = None，fdel = None，doc = None ）
返回属性属性。

fget是获取属性值的函数。 fset是设置属性值的函数。fdel是删除属性值的功能。然后doc为该属性创建一个文档字符串。

一个典型的用途是定义一个托管属性x：

 C 类：
    def  __init__ （self ）：
        self 。_x  =  无

    def  getx （self ）：
        返回 自我。_X

    def  setx （self ， value ）：
        self 。_x  =  值

    def  delx （self ）：
        del  self 。_X

    x  =  property （getx ， setx ， delx ， “我是'x'属性。” ）
如果c是C的一个实例，c.x将调用getter， 将调用setter和deleter。c.x = valuedel c.x

如果给定，doc将是属性属性的文档字符串。否则，该属性将复制fget的文档字符串（如果存在）。这使得可以使用property()作为装饰器轻松地创建只读属性：

class  Parrot ：
    def  __init__ （self ）：
        self 。_voltage  =  100000

    @property
    def  voltage （self ）：
        “”“获取当前电压。”“”
        返回 自我。_电压
该@property装饰变成的voltage()方法变成“吸”为只读具有相同名称的属性，并将其设置的文档字符串的 电压为“获取当前的电压。”

一个属性对象具有getter，setter以及deleter可用作为创建属性的副本设置为装饰功能相应的存取功能的装饰方法。最好用一个例子来解释：

 C 类：
    def  __init__ （self ）：
        self 。_x  =  无

    @property
    def  x （self ）：
        “”“我是'x'属性。”“”
        return  self 。_X

    @x 。setter
    def  x （self ， value ）：
        自我。_x  =  值

    @x 。deleter
    def  x （self ）：
        del  self 。_X
这段代码和第一个例子完全相同。一定要赋予与原始属性相同名称的附加功能（x在这种情况下）。

返回的属性对象也有属性fget，fset以及 fdel相对应的构造函数的参数。

在版本3.5中更改：属性对象的文档现在是可写的。




6.666666
locals 介绍

复制代码
复制代码
 1 >>> def test(arg):
 2 #函数 foo 在它的局部名字空间中有两个变量：arg（它的值被传入函数），和 z（它是在函数里定义的）。
 3     z = 1
 4     print locals()
 5 >>> test(4)
 6 #locals 返回一个名字/值对的字典。这个字典的键字是字符串形式的变量名字，字典的值是变量的实际值。
 7 #所以用 4 来调用 foo，会打印出包含函数两个局部变量的字典：arg (4) 和 z (1)。
 8 {'z': 1, 'arg': 4}
 9 >>> test('doulaixuexi')
10 #locals 可以用于所有类型的变量。
11 {'z': 1, 'arg': 'doulaixuexi'}


7.777777
globals 介绍

复制代码
按 Ctrl+C 复制代码

>>> from sys import *
>>> print globals()
{'setrecursionlimit': <built-in function setrecursionlimit>,
'dont_write_bytecode': False,
'getfilesystemencoding': <built-in function getfilesystemencoding>,
'long_info': sys.long_info(bits_per_digit=15, sizeof_digit=2),
'stdout': <idlelib.rpc.RPCProxy object at 0x02110850>,
'text': <function text at 0x02111A70>,
'meta_path': [],
'exc_clear': <built-in function exc_clear>,
'prefix': 'C:\\Python27', 'getrefcount': <built-in function getrefcount

80888888888888
dir()和vars()的区别就是：dir()只打印属性，vars()则打印属性与属性的值。
[python] view plain copy
a='abcdefg'
class B():
    c='djfj'

print dir()
print vars()
print dir(B)
print vars(B)
结果：
['B', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a']
{'a': 'abcdefg', 'B': <class __main__.B at 0x02A2DD88>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'E:\\workspace\\python day03\\main\\test.py', '__package__': None, '__name__': '__main__', '__doc__': None}
['__doc__', '__module__', 'c']
{'__module__': '__main__', 'c': 'djfj', '__doc__': None}
[python] view plain copy
>>> class C(object):
        f=2


>>> dir(C)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'f']
>>> vars(C)
dict_proxy({'__dict__': <attribute '__dict__' of 'C' objects>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None, 'f': 2})
>>> C.__dict__
dict_proxy({'__dict__': <attribute '__dict__' of 'C' objects>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None, 'f': 2})
>>> c=C()
>>> dir(c)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'f']
>>> vars(c)
{}
>>> c.__dict__
{}
>>>

以下实例展示了 vars() 的使用方法：

>>>print(vars())
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> class Runoob:
...     a = 1
...
>>> print(vars(Runoob))
{'a': 1, '__module__': '__main__', '__doc__': None}
>>> runoob = Runoob()
>>> print(vars(runoob))
{}
1.认识dir()

功能：查看指定模块的功能列表，以及任意指定对象的功能列表。

例如：

import re

dir(re)

['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTIL
INE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACH
E', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__'
, '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alp
hanum_str', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_l
ocale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'error', 'esc
ape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', '
sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']

例如：

d = []

dir(d)


'''


#
# import  struct
# dir ()
#
# print(dir(struct))
# __all__'，__builtins__，__cached__，__doc__，
# __file__，__initializing
# __，__loader__，__name__，__package__，_clearcache，calcsize，error， 'pack'，'pack_into'，'unpack'，'unpack_from']
# >>> class  Shape ：
# ...    def  __dir__ （self ）：
# ...         return  [ 'area' ， 'perimeter' ， 'location' ]
# >>> s  =  Shape （）
# >>> dir （s ）
# ['area'，'location'，'perimeter']
# 注意 由于dir()主要是为了方便在交互提示中使用，因此它试图提供一组有趣的名称，而不是试图提供严格或一致定义的名称集，而且其详细行为可能会在不同版本之间发生变化。例如，当参数是一个类时，元类属性不在结果列表中。
#
# getattr()函数是Python自省的核心函数，具体使用大体如下：
#
# 获取对象引用getattr
# Getattr用于返回一个对象属性，或者方法
# def foo(arg, a):
#   x = 100
#   y = 'hello python!'
#   for i in range(10):
#     j = 1
#     k = i
#   print(locals())
#
# foo(1, 2)

# a=[{'id':1,'name':'zhu1','pid':0},{'id':2,'name':'zhu2','pid':0},{'id':3,'name':'1sub1','pid':1},{'id':4,'name':'1sub4','pid':1},{'id':5,'name':'2sub1','pid':3}]
# def tojson(sr=None,sc=[]):
# 	if sc:
# 		for i in sc:
# 			for j in sr:
# 				if i['id']==j['pid']:i['sub'].append(j)
# 			if i['sub']:tojson(sr,i['sub'])
# 	else:
# 		for i in sr:
# 			i['sub']=[]
# 			if i['pid']==0:sc.append(i)
# 		tojson(sr,sc)
# b=[]
# tojson(a,b)
# print(b)
# from  ds_goods.models import TypeInfo
# import json
# from django.core import serializers
# import json
# def jhj(request):
#   x= request.session['typeinfos']=json.loads(serializers.serialize('json',TypeInfo.objects.all()))
#   print(x)
#   def tojson(sr=None, sc=[]):
#     if sc:
#       for i in sc:
#         for j in sr:
#           if i['id'] == j['pid']: i['sub'].append(j)
#         if i['sub']: tojson(sr, i['sub'])
#     else:
#       for i in sr:
#         i['sub'] = []
#         if i['pid'] == 0: sc.append(i)
#       tojson(sr, sc)
#
#   b = []
#   tojson(x, b)
#   print(b)


