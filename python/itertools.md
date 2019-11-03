Python循环这样写，高效节省内存100倍

### 0 前言

说到处理循环，我们习惯使用for, while等，比如依次打印每个列表中的字符：

```
lis = ['I', 'love', 'python']
for i in lis:
	print(i)
I
love
python
```

在打印内容字节数较小时，全部载入内存后，再打印，没有问题。可是，如果现在有成千上百万条车辆行驶轨迹，叫你分析出其中每个客户的出行规律，堵车情况等，假如是在单机上处理这件事。



你可能首先要面临，也可能被你忽视，最后代码都写好后，才可能暴露出的一个问题:`outofmemory`, 这在实际项目中经常遇到。



这个问题提醒我们，处理数据时，如何写出高效利用内存的程序，就显得很重要。今天，我们就来探讨如何高效利用内存，节省内存同时还能把事情办好。



其实，Python已经准备好一个模块专门用来处理这件事，它就是 `itertools` 模块，这里面几个函数的功能其实很好理解。



我不打算笼统的介绍它们所能实现的功能，而是想分析这些功能背后的实现代码，它们如何做到高效节省内存的，Python内核的贡献者们又是如何写出一手漂亮的代码的，这很有趣，不是吗？



OK，let's go. Hope you enjoy the journey!



### 1 拼接元素

itertools 中的chain 函数实现元素拼接，原型如下，参数*表示个数可变的参数

`chain`(*iterables*)

应用如下：

```
In [33]: list(chain(['I','love'],['python'],['very', 'much']))
Out[33]: ['I', 'love', 'python', 'very', 'much']
```

哇，不能再好用了，它有点join的味道，但是比join强，它的重点在于参数都是可迭代的实例。

那么，chain如何实现高效节省内存的呢？chain大概的实现代码如下：

```python
def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element
```

以上代码不难理解，`chain本质返回一个生成器，所以它实际上是一次读入一个元素到内存，所以做到最高效地节省内存`。



### 2 逐个累积

返回列表的累积汇总值，原型：

`accumulate`(*iterable*[, *func*, \*, *initial=None*])

应用如下：

```
In [36]: list(accumulate([1,2,3,4,5,6],lambda x,y: x*y))
Out[36]: [1, 2, 6, 24, 120, 720]
```

accumulate大概的实现代码如下：

```python
def accumulate(iterable, func=operator.add, *, initial=None):
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total
```

以上代码，你还好吗？与chain简单的yield不同，此处稍微复杂一点，yield有点像return，所以 `yield total`那行直接就返回一个元素，也就是iterable的第一个元素，因为任何时候这个函数返回的第一个元素就是它的第一个。又因为yield返回的是一个generator对象，比如名字gen，所以next(gen)时，代码将会执行到 ` for element in it:`这行，而此时的迭代器it 已经指到iterable的第二个元素，OK，相信你懂了！



### 3 漏斗筛选

它是compress 函数，功能类似于漏斗功能，所以我称它为漏斗筛选，原型：

`compress`(*data*, *selectors*)

```
In [38]: list(compress('abcdefg',[1,1,0,1]))
Out[38]: ['a', 'b', 'd']
```

容易看出，compress返回的元素个数等于两个参数中较短的列表长度。

它的大概实现代码：

```
def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)
```

这个函数非常好用

### 4 段位筛选

扫描列表，不满足条件处开始往后保留，原型如下：

`dropwhile`(*predicate*, *iterable*)

应用例子：

```
In [39]: list(dropwhile(lambda x: x<3,[1,0,2,4,1,1,3,5,-5]))
Out[39]: [4, 1, 1, 3, 5, -5]
```

实现它的大概代码如下：

```python
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```



### 5 段位筛选2

扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止，原型如下：

`takewhile`(*predicate*, *iterable*)

应用例子：

```
In [43]: list(takewhile(lambda x: x<5, [1,4,6,4,1]))
Out[43]: [1, 4]
```

实现它的大概代码如下：

```
def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break #立即返回
```



### 6 次品筛选

扫描列表，只要不满足条件都保留，原型如下：

`dropwhile`(*predicate*, *iterable*)

应用例子：

```
In [40]: list(filterfalse(lambda x: x%2==0, [1,2,3,4,5,6]))
Out[40]: [1, 3, 5]
```

实现它的大概代码如下：

```
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

### 7 切片筛选

Python中的普通切片操作，比如：

```
lis = [1,3,2,1]
lis[:1]
```

它们的缺陷还是lis 必须全部载入内存，所以更节省内存的操作islice，原型如下：

`islice`(*iterable*, *start*, *stop*[, *step*])

应用例子：

```python
In [41]: list(islice('abcdefg',1,4,2))
Out[41]: ['b', 'd']
```

实现它的大概代码如下：

```python
def islice(iterable, *args):
    s = slice(*args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(it)
    except StopIteration:
        for i, element in zip(range(start), iterable):
            pass
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(it)
    except StopIteration:
        for i, element in zip(range(i + 1, stop), iterable):
            pass
```

巧妙利用生成器迭代结束时会抛出异常`StopIteration`，做一些边界处理的事情。

### 8 细胞分裂

tee函数类似于我们熟知的细胞分裂，它能复制原迭代器n个，原型如下：

`tee`(*iterable*, *n=2*)

应用如下，可以看出复制出的两个迭代器是独立的

```
a = tee([1,4,6,4,1],2)
In [51]: next(a[0])
Out[51]: 1

In [52]: next(a[1])
Out[52]: 1
```

实现它的代码大概如下：

```python
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:            
                try:
                    newval = next(it)   
                except StopIteration:
                    return
                for d in deques:     
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)
```

tee 实现内部使用一个队列类型deques，起初生成空队列，向复制出来的每个队列中添加元素newval, 同时yield 当前被调用的mydeque中的最左元素。

### 9 map变体

starmap可以看做是map的变体，它能更加节省内存，同时iterable的元素必须也为可迭代对象，原型如下：

`starmap`(*function*, *iterable*)

应用它：

```
In [63]: list(starmap(lambda x,y: str(x)+'-'+str(y), [('a',1),('b',2),('c',3)]))
Out[63]: ['a-1', 'b-2', 'c-3']
```

starmap的实现细节如下：

```
def starmap(function, iterable):
    for args in iterable:
        yield function(*args)
```

### 10 复制元素

repeat实现复制元素n次，原型如下：

`repeat`(*object*[, *times*])

应用如下：

```
In [66]: list(repeat(6,3))
Out[66]: [6, 6, 6]

In [67]: list(repeat([1,2,3],2))
Out[67]: [[1, 2, 3], [1, 2, 3]]
```

它的实现细节大概如下：

```
def repeat(object, times=None):
    if times is None:# 如果times不设置，将一直repeat下去
        while True: 
            yield object
    else:
        for i in range(times):
            yield object
```

### 11 笛卡尔积

笛卡尔积实现的效果同下：

```
 ((x,y) for x in A for y in B)
```

所以，笛卡尔积的实现效果如下：

```
In [68]: list(product('ABCD', 'xy'))
Out[68]:
[('A', 'x'),
 ('A', 'y'),
 ('B', 'x'),
 ('B', 'y'),
 ('C', 'x'),
 ('C', 'y'),
 ('D', 'x'),
 ('D', 'y')]
```

它的实现细节：

```
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```

### 12 加强版zip

组合值。若可迭代对象的长度未对齐，将根据 *fillvalue* 填充缺失值，注意：`迭代持续到耗光最长的可迭代对象`，效果如下：

```
In [69]: list(zip_longest('ABCD', 'xy', fillvalue='-'))
Out[69]: [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]

```

它的实现细节：

```python
def zip_longest(*args, fillvalue=None):
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)
```

它里面使用repeat，也就是在可迭代对象的长度未对齐时，根据 *fillvalue* 填充缺失值。理解上面代码的关键是迭代器对象(iter)，next方法的特殊性：

```
In [74]: for i, it in enumerate([iter([1,2,3]),iter(['x','y'])]):
    ...:     print(next(it))
    #输出：
    1
	x
```

结合这个提示再理解上面代码，就不会吃力。

### 总结

Python的itertools模块提供的节省内存的高效迭代器，里面实现基本都借助于生成器，所以一方面了解这12个函数所实现的基本功能，同时也能加深对生成器(generator)的理解，为我们写出更加高效、简洁、漂亮的代码打下坚实基础。

