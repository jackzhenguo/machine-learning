Python中对象之间的比较，可以用 ==，也可以用 is. 在实际使用时，该如何选用。

先记住两点：

1) == 比较的是两个对象的**内容是否相等**，即内存地址可以不一样，内容一样就可以了。

2) is 比较的是两个实例对象内存地址是否一样



下面，结合最经典的例子，让大家在最短的时间内快速领悟最本质的知识点。



### is 

`is` 比较的是两个对象的内存地址是否相同。在python中，内存地址查看方法：

1

```
In [1]: a = [1,2,3]

In [2]: id(a) #获取列表实例 a在内存中的地址
Out[2]: 95219592
```

2

```
In [5]: b = [1,2,3] #再创建一个列表实例，元素取值也为 1,2,3

In [6]: id(b) 
Out[6]: 95165640
```

3

```
In [7]: a is b # is操作符本质上判断a 和 b的内存地址是否相等
Out[7]: False
```

4

```
In [8]: b = a # 令b 指向 a，此时b is a 返回 true

In [9]: b is a
Out[9]: True
```



### in

`in`是判断是否包含，判断一个集合(如`list、tuple`)是否包含这个元素

5 

```
In [70]: 'ab' in 'abc'
Out[70]: True

In [71]: 'ab' in 'acb'
Out[71]: False
```



6

```
In [72]: print([1,2] in [[1,2],'str'])
True
```

7

字典只能判断key 存不存在

```
In [73]: print('abc' in {'abc':12})
True

In [74]: print('12' in {'abc':12})
False
```



###  ==

**==** 判断值是否相等，等不等关系。

8

```
In [75]: str1 = "alg-channel"

In [76]: str2 = "alg-channel"

In [77]: print(str1 == str2)
True
```



9

```
In [78]: a = [1, 2, 3]

In [79]: b = [1, 2, 4]

In [80]: a == b
Out[80]: False
```



### 扩展



目前最常使用 is 的地方是判断对象是否为 None：

10

```
In [78]: a = [1, 2, 3]
In [81]: a is None
Out[81]: False

In [82]: None is None
Out[82]: True
```

11

`== ` 默认调用对象的`__eq__()`方法。继承自`object`对象的`__eq__()`方法直接比较两个对象的id.  很不幸，很多实际场景中，与我们期望相悖。

```python
class Student(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __eq__(self, *args, **kwargs):
        return object.__eq__(self, *args, **kwargs)

xiaoming = student(25, "xiaoming")
xueming = student(23, "xueming")
xiaoming2 = student(25,"xiaoming")

print(xiaoming is xiaoming2) #False
print(xiaoming == xiaoming2) #False
print(xiaoming is xueming) #False

```

xiaoming和xiaoming2的属性一致，期望判断出他们是同一人，但是不管is 还是 == 都比较了id是否相等。需要重写 `== ` 操作符默认调用的`__eq__()`方法

```python
	def __eq__(self,other):
		return self.id == other.id and self.name == other.name
```



大多数时候继承`object`的类会覆盖`__eq__()`方法，比较自定义对象的值可能更有用。

12 

不要觉得意外，一切都是为了性能更优。知道细节的小伙伴欢迎留言

```python
In [100]: a = 123

In [101]: b = 123

In [102]: a is b
Out[102]: True

In [103]: c = 123456

In [104]: d = 123456

In [105]: c is d
Out[105]: False

In [106]: id(c)
Out[106]: 94480720

In [107]: id(d)
Out[107]: 94481200
```




