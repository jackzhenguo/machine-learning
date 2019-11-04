1 abs()

绝对值或复数的模

```
In [1]: abs(-6)
Out[1]: 6
```

2 all()　　

接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False

```
In [2]: all([1,0,3,6])
Out[2]: False

In [3]: all([1,2,3])
Out[3]: True
```

3 any()　　

接受一个迭代器，如果迭代器里有一个元素为真，那么返回True，否则返回False

```
In [4]: any([0,0,0,[]])
Out[4]: False

In [5]: any([0,0,1])
Out[5]: True
```

4 ascii()　　

调用对象的__repr__() 方法，获得该方法的返回值

```
In [30]: class Student():
    ...:     def __init__(self,id,name):
    ...:         self.id = id
    ...:         self.name = name
    ...:     def __repr__(self):
    ...:         return 'id = '+self.id +', name = '+self.name
    
In [33]: print(xiaoming)
id = 001, name = xiaoming

In [34]: ascii(xiaoming)
Out[34]: 'id = 001, name = xiaoming'
```

5  bin()

将十进制转换为二进制

```
In [35]: bin(10)
Out[35]: '0b1010'
```

6 oct()

将十进制转换为八进制

```
In [36]: oct(9)
Out[36]: '0o11'
```

7 hex()

将十进制转换为十六进制

```
In [37]: hex(15)
Out[37]: '0xf'
```

8 bool()　　

测试一个对象是True, 还是False.

```
In [38]: bool([0,0,0])
Out[38]: True

In [39]: bool([])
Out[39]: False

In [40]: bool([1,0,1])
Out[40]: True
```

9 bytes()　　

将一个字符串转换成字节类型

```
In [44]: s = "apple"

In [45]: bytes(s,encoding='utf-8')
Out[45]: b'apple'
```

10 str()　　

将`字符类型`、`数值类型`等转换为字符串类型

```
In [46]: integ = 100

In [47]: str(integ)
Out[47]: '100'
```

11 callable()　　

判断对象是否可以被调用，能被调用的对象就是一个callable 对象，比如函数 str, int 等都是可被调用的，但是例子4 中xiaoming这个实例是不可被调用的：

```
In [48]: callable(str)
Out[48]: True

In [49]: callable(int)
Out[49]: True

In [50]: xiaoming
Out[50]: id = 001, name = xiaoming

In [51]: callable(xiaoming)
Out[51]: False
```

12 chr()

查看十进制整数对应的ASCII字符

```
In [54]: chr(65)
Out[54]: 'A'
```

13 ord()

查看某个ascii对应的十进制数

```
In [60]: ord('A')
Out[60]: 65
```

14 classmethod()　　

**classmethod** 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

```
In [66]: class Student():
    ...:     def __init__(self,id,name):
    ...:         self.id = id
    ...:         self.name = name
    ...:     def __repr__(self):
    ...:         return 'id = '+self.id +', name = '+self.name
    ...:     @classmethod
    ...:     def f(cls):
    ...:         print(cls)
```

15 complie()　　

将字符串编译成python 能识别或可以执行的代码，也可以将文字读成字符串再编译。

```
In [74]: s  = "print('helloworld')"

In [75]: r = compile(s,"<string>", "exec")

In [76]: r
Out[76]: <code object <module> at 0x0000000005DE75D0, file "<string>", line 1>

In [77]: exec(r)
helloworld
```

16  complex()

创建一个复数

```
In [81]: complex(1,2)
Out[81]: (1+2j)
```

17 delattr()　　

删除对象的属性

```
In [87]: delattr(xiaoming,'id')

In [88]: hasattr(xiaoming,'id')
Out[88]: False
```

18 dict()　　

创建数据字典

```
In [92]: dict()
Out[92]: {}

In [93]: dict(a='a',b='b')
Out[93]: {'a': 'a', 'b': 'b'}

In [94]: dict(zip(['a','b'],[1,2]))
Out[94]: {'a': 1, 'b': 2}

In [95]: dict([('a',1),('b',2)])
Out[95]: {'a': 1, 'b': 2}
```

19 dir()　　

不带参数时返回当前范围内的变量，方法和定义的类型列表；带参数时返回参数的属性，方法列表。

```
In [96]: dir(xiaoming)
Out[96]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 
 'name']
```

20 divmod()　　

分别取商和余数

```
In [97]: divmod(10,3)
Out[97]: (3, 1)
```

21 enumerate()　　

返回一个可以枚举的对象，该对象的next()方法将返回一个元组。

```
In [98]: s = ["a","b","c"]
    ...: for i ,v in enumerate(s,1):
    ...:     print(i,v)
    ...:
1 a
2 b
3 c
```

22 eval()　　

将字符串str 当成有效的表达式来求值并返回计算结果取出字符串中内容

```
In [99]: s = "1 + 3 +5"
    ...: eval(s)
    ...:
Out[99]: 9
```

23 exec()　　

执行字符串或complie方法编译过的字符串，没有返回值

```
In [74]: s  = "print('helloworld')"

In [75]: r = compile(s,"<string>", "exec")

In [76]: r
Out[76]: <code object <module> at 0x0000000005DE75D0, file "<string>", line 1>

In [77]: exec(r)
helloworld
```

24 filter()　　

过滤器，构造一个序列，等价于

```
[ item for item in iterables if function(item)]
```

在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。

```
In [101]: fil = filter(lambda x: x>10,[1,11,2,45,7,6,13])

In [102]: list(fil)
Out[102]: [11, 45, 13]
```

25 float()　　

将一个字符串或整数转换为浮点数

```
In [103]: float(3)
Out[103]: 3.0
```

26 format()　　

格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。

```
In [104]: print("i am {0},age{1}".format("tom",18))
i am tom,age18
```

27 frozenset()　　

创建一个不可修改的集合。

```
In [105]: frozenset([1,1,3,2,3])
Out[105]: frozenset({1, 2, 3})
```

28 getattr()　　

获取对象的属性

```
In [106]: getattr(xiaoming,'name')
Out[106]: 'xiaoming'
```

29 globals()　　

返回一个描述当前全局变量的字典

30 hasattr()

```
In [110]: hasattr(xiaoming,'name')
Out[110]: True

In [111]: hasattr(xiaoming,'id')
Out[111]: False
```

31 hash()　　

返回对象的哈希值

  ```
In [112]: hash(xiaoming)
Out[112]: 6139638
  ```

32 help()　　

返回对象的帮助文档

```
In [113]: help(xiaoming)
Help on Student in module __main__ object:

class Student(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self, id, name)
 |
 |  __repr__(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

33 id()　　

返回对象的内存地址

```
In [115]: id(xiaoming)
Out[115]: 98234208
```

34 input()　　

获取用户输入内容

```
In [116]: input()
aa
Out[116]: 'aa'
```

35  int()　　

int(x, base =10) , x可能为字符串或数值，将x 转换为一个普通整数。如果参数是字符串，那么它可能包含符号和小数点。如果超出了普通整数的表示范围，一个长整数被返回。  

```
In [120]: int('12',16)
Out[120]: 18
```

<<<<<<< HEAD
=======
36  isinstance(*object*, *classinfo*)

判断*object*是否为类*classinfo*的实例，是返回true

```
In [20]: class Student():
    ...:     ...:     def __init__(self,id,name):
    ...:     ...:         self.id = id
    ...:     ...:         self.name = name
    ...:     ...:     def __repr__(self):
    ...:     ...:         return 'id = '+self.id +', name = '+self.name
    ...:

In [21]: xiaoming = Student('001','xiaoming')

In [22]: isinstance(xiaoming,Student)
Out[22]: True
```

37 issubclass(*class*, *classinfo*)

如果class是classinfo类的子类，返回True：

```
In [27]: class undergraduate(Student):
    ...:     def studyClass(self):
    ...:         pass
    ...:     def attendActivity(self):
    ...:         pass
    ...:

In [28]: issubclass(undergraduate,Student)
Out[28]: True

In [29]: issubclass(object,Student)
Out[29]: False

In [30]: issubclass(Student,object)
Out[30]: True
```

如果class是classinfo元组中某个元素的子类，也会返回True

```

In [26]: issubclass(int,(int,float))
Out[26]: True
```

38 iter(object, sentinel)

返回一个可迭代对象, sentinel可省略

```
In [72]: lst = [1,3,5]

In [73]: for i in iter(lst):
    ...:     print(i)
    ...:
1
3
5
```

sentinel 理解为迭代对象的哨兵，一旦迭代到此元素，立即终止：

```
In [81]: class TestIter(object):
    ...:         def __init__(self):
    ...:             self.l=[1,3,2,3,4,5]
    ...:             self.i=iter(self.l)
    ...:         def __call__(self):  #定义了__call__方法的类的实例是可调用的
    ...:             item = next(self.i)
    ...:             print ("__call__ is called,which would return",item)
    ...:             return item
    ...:         def __iter__(self): #支持迭代协议(即定义有__iter__()函数)
    ...:             print ("__iter__ is called!!")
    ...:             return iter(self.l)
    ...:

In [82]:     t = TestIter()
    ...:     t1 = iter(t, 3)
    ...:     for i in t1:
    ...:         print(i)
    ...:
__call__ is called,which would return 1
1
__call__ is called,which would return 3
```

39 len(*s*)

返回对象的长度（元素个数）

```
In [83]: dic = {'a':1,'b':3}

In [84]: len(dic)
Out[84]: 2
```

40 list([*iterable*])

返回可变序列类型

```
In [85]: list(map(lambda x: x%2==1, [1,3,2,4,1]))
Out[85]: [True, True, False, False, True]
```

41 map(*function*, *iterable*, *...*)

返回一个将 *function* 应用于 *iterable* 中每一项并输出其结果的迭代器：

```
In [85]: list(map(lambda x: x%2==1, [1,3,2,4,1]))
Out[85]: [True, True, False, False, True]
```

可以传入多个*iterable*对象，输出长度等于最短序列的长度：

```
In [88]: list(map(lambda x,y: x%2==1 and y%2==0, [1,3,2,4,1],[3,2,1,2]))
Out[88]: [False, True, False, False]
```

42 max(*iterable*,\*[, *key*, *default*])

返回最大值：

```
In [99]: max(3,1,4,2,1)
Out[99]: 4

In [100]: max((),default=0)
Out[100]: 0

In [89]: di = {'a':3,'b1':1,'c':4}
In [90]: max(di)
Out[90]: 'c'

In [102]: a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'
     ...: xiaohong','age':20,'gender':'female'}]
In [104]: max(a,key=lambda x: x['age'])
Out[104]: {'name': 'xiaohong', 'age': 20, 'gender': 'female'}

```

43 min(*iterable*,\*[, *key*, *default*])

返回最小值

44 memoryview(*obj*)

返回由给定实参创建的“内存视图”对象， Python 代码访问一个对象的内部数据，只要该对象支持 *缓冲区协议* 而无需进行拷贝

45 next(*iterator*,[, *default*])

返回可迭代对象的下一个元素

```
In [129]: it = iter([5,3,4,1])

In [130]: next(it)
Out[130]: 5

In [131]: next(it)
Out[131]: 3

In [132]: next(it)
Out[132]: 4

In [133]: next(it)
Out[133]: 1

In [134]: next(it,0) #迭代到头，默认返回值为0
Out[134]: 0

In [135]: next(it)
----------------------------------------------------------------------
StopIteration                        Traceback (most recent call last)
<ipython-input-135-bc1ab118995a> in <module>
----> 1 next(it)

StopIteration:
```

46 object()

返回一个没有特征的新对象。object 是所有类的基类。

```
In [137]: o = object()

In [138]: type(o)
Out[138]: object
```

47 open(*file*)

返回文件对象

```
In [146]: fo = open('D:/a.txt',mode='r', encoding='utf-8')

In [147]: fo.read()
Out[147]: '\ufefflife is not so long,\nI use Python to play.'
```

mode取值表：

| 字符  | 意义                             |
| :---- | :------------------------------- |
| `'r'` | 读取（默认）                     |
| `'w'` | 写入，并先截断文件               |
| `'x'` | 排它性创建，如果文件已存在则失败 |
| `'a'` | 写入，如果文件存在则在末尾追加   |
| `'b'` | 二进制模式                       |
| `'t'` | 文本模式（默认）                 |
| `'+'` | 打开用于更新（读取与写入）       |

48 pow(*base*, *exp*[, *mod*])

base为底的exp次幂，如果mod给出，取余

```
In [149]: pow(3, 2, 4)
Out[149]: 1
```

49 print(objects)

打印对象，此函数不解释

50 *class* property(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

返回 property 属性，典型的用法：

```
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    # 使用property类创建 property 属性
    x = property(getx, setx, delx, "I'm the 'x' property.")
```

使用python装饰器，实现与上完全一样的效果代码：

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

51 range(stop) 

range(start, stop[,step])

生成一个不可变序列：

```
In [153]: range(11)
Out[153]: range(0, 11)

In [154]: range(0,11,1)
Out[154]: range(0, 11)
```

52 reversed(*seq*)

返回一个反向的 iterator:

```
In [155]: rev = reversed([1,4,2,3,1])

In [156]: for i in rev:
     ...:     print(i)
     ...:
1
3
2
4
1
```

53 round(*number*[, *ndigits*])

四舍五入，ndigits代表小数点后保留几位：

```
In [157]: round(10.0222222, 3)
Out[157]: 10.022
```

54 *class* set([*iterable*])

返回一个set对象，可实现去重：

```
In [159]: a = [1,4,2,3,1]

In [160]: set(a)
Out[160]: {1, 2, 3, 4}
```

55 class slice(*stop*)

*class* slice(*start*, *stop*[, *step*])

返回一个表示由 range(start, stop, step) 所指定索引集的 slice对象

```
In [170]: a = [1,4,2,3,1]

In [171]: a[slice(0,5,2)] #等价于a[0:5:2]
Out[171]: [1, 2, 1]
```

56 sorted(*iterable*, \*, *key=None*, *reverse=False*)

排序：

```
In [174]: a = [1,4,2,3,1]

In [175]: sorted(a,reverse=True)
Out[175]: [4, 3, 2, 1, 1]

In [178]: a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'
     ...: xiaohong','age':20,'gender':'female'}]
In [180]: sorted(a,key=lambda x: x['age'],reverse=False)
Out[180]:
[{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
 {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]
```

57 @``staticmethod`

将方法转换为静态方法，不做解释

58 vars()

返回模块、类、实例或任何其它具有 `__dict__`属性的对象的 `__dict__` 属性

```
In [2]: vars()
Out[2]:
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['', 'vars([1,2,3])', 'vars()'],
 '_oh': {},
 '_dh': ['C:\\Windows\\system32'],
 'In': ['', 'vars([1,2,3])', 'vars()'],
 'Out': {},
 'get_ipython': <bound method InteractiveShell.get_ipython of <IPython.terminal.interactiveshell.TerminalInteractiveShell object at 0x0000026004D91C50>>,
 'exit': <IPython.core.autocall.ExitAutocall at 0x26006011048>,
 'quit': <IPython.core.autocall.ExitAutocall at 0x26006011048>,
 '_': '',
 '__': '',
 '___': '',
 '_i': 'vars([1,2,3])',
 '_ii': '',
 '_iii': '',
 '_i1': 'vars([1,2,3])',
 '_i2': 'vars()'}
```





59 sum(*iterable*, */*, *start=0*)

求和：

```
In [181]: a = [1,4,2,3,1]

In [182]: sum(a)
Out[182]: 11

In [185]: sum(a,10) #求和的初始值为10
Out[185]: 21
```

60 super([*type*[, *object-or-type*]])

返回一个代理对象，它会将方法调用委托给 *type* 的父类或兄弟类

61 tuple([*iterable*])

虽然被称为函数，但 `tuple` 实际上是一个不可变的序列类型

62 *class* `type`(*object*)

*class* `type`(*name*, *bases*, *dict*)

传入一个参数时，返回 *object* 的类型：

```
In [186]: type(xiaoming)
Out[186]: __main__.Student

In [187]: type(tuple())
Out[187]: tuple
```

63 `zip`(**iterables*)

创建一个聚合了来自每个可迭代对象中的元素的迭代器：

```
In [188]: x = [3,2,1]
In [189]: y = [4,5,6]
In [190]: list(zip(y,x))
Out[190]: [(4, 3), (5, 2), (6, 1)]


In [191]: a = range(5)
In [192]: b = list('abcde')
In [193]: b
Out[193]: ['a', 'b', 'c', 'd', 'e']
In [194]: [str(y) + str(x) for x,y in zip(a,b)]
Out[194]: ['a0', 'b1', 'c2', 'd3', 'e4']
```

>>>>>>> 3ab5835554c54aa00eb79430f9e7b3a63cf3d12a
