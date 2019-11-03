Python有许多很好的库(libraries)，实现这些功能只需要几行代码。今天介绍一个库：*collections*. 这个模块提供容器相关的更高性能的数据类型，它们提供比通用容器 *dict*, *list*, *set* 和*tuple*更强大的功能。

今天介绍其中三种数据类型，最后你可能会惊讶它们怎么这么好用。

### NamedTuple

对于数据分析或机器学习领域，用好namedtuples 会写出可读性强、易于维护的代码。大家回忆这种熟悉的场景，你正在做特征工程，因为你尤其喜爱list, 所以把一堆特征放到一个list 中，然后喂到机器学习模型中。很快，你将会意识到数百个特征位于此list 中，这就是事情变得糟糕的开始。

```python
In [10]: feature = ['age','height','name']

In [11]: data = [[10,1,'xiaoming'],[12,1,5,'xiaohong']]

In [12]: data[0][0] #只能靠整数索引到某个特征，0对应age
Out[12]: 10
```



某天，你想使用某个特征，这时比较棘手，你不知道它的index！ 更糟糕的是，当你准备离职要交接工作时，他们看到一个一个的数字型索引，完全对不上哪个和哪个，他们懵逼，你也尴尬。

如果我们使用NamedTuples去处理以上数据，乱为一团的事情将会迅速变得井然有序：

```python
In [4]: Person = namedtuple('Person',['age','height','name'])
In [15]: data2 = [Person(10,1.4,'xiaoming'),Person(12,1.5,'xiaohong')]
In [16]: data2[0].age
Out[16]: 10
```

仅仅几行代码，我们将会很容易索引到第0行数据的age属性取值，这在实际中真是太好用。你告别indexes访问你的数据集中的特征值，而是使用更加人性化，可读性强的names索引。

NamedTuples会使得代码易读、更易维护。 

### Counter

Counter正如名字那样，它的主要功能就是计数。这听起来简单，但是我们在分析数据时，基本都会涉及计数，真的家常便饭。

习惯使用list 的看过来，有一些数值已经放在一个list中：

```python
skuPurchaseCount = [3, 8, 3, 10, 3, 3, 1, 3, 7, 6, 1, 2, 7, 0, 7, 9, 1, 5, 1, 0]
In [33]: for i in skuPurchaseCount:
    ...:     if countdict.get(i) is None:
    ...:         countdict[i]=1
    ...:     else:
    ...:         countdict[i]+=1
In [34]: countdict
Out[34]: {3: 5, 8: 1, 10: 1, 1: 4, 7: 3, 6: 1, 2: 1, 0: 2, 9: 1, 5: 1}
```

如果使用Counter，我们可以写出更简化的代码：

```
In [35]: from collections import Counter
In [42]: Counter(skuPurchaseCount).most_common()
Out[42]:
[(3, 5),(1, 4),(7, 3),(0, 2),(8, 1),(10, 1),(6, 1),(2, 1),(9, 1),(5, 1)]
```

仅仅一行代码，我们便输出统计计数结果，并且是一个按照次数统计出来的由大到小排序好的tuples列表，因此我们很快就会看到，购买3次是出现最多的，一共5次。

购买为1次的占多数，属于长尾。

### DefaultDict

DefaultDict是一个被初始化的字典，也就是每个键都已经被访问一次：

```python
In [53]: d = defaultdict(int)
In [54]: for k in 'collections':
    ...:     d[k] += 1
In [55]: d
Out[55]:
defaultdict(int,
            {'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1})
```

一般地，当你尝试访问一个不在字典中的值时，将会抛出一个异常。但是defaultdict可以帮助我们初始化，它的参数作为default_factory. 在上面例子中，将生成 `int`对象，意思是默认值为int 型，并`设定初始值为0`，所以我们可以很容易地统计每个字符出现的次数。

Simple and clean!

更有用的一个使用场景，我们有很多种商品，在每秒内下单次数的统计数据如下：

```python
In [56]: data = [('iphone11',103), ('华为macbook-SKU1232',210),('iphone11',21),('
    ...: 华为macbook-SKU1232',100)]
In [57]: d = defaultdict(list)
In [58]: for ele in data:
    ...:     d[ele[0]].append(ele[1])
In [59]: d
Out[59]: defaultdict(list, {'iphone11': [103, 21], '华为macbook-SKU1232': [210, 100]})
```

上面例子default_dict取值为list, 因此，我们可以立即append一个元素到list中，更简洁。



总结

至此，你已经了解collections库中的三个类型，它们确实太好用，大家可以操练起来了！

