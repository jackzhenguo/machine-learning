太好了，一分钟带你分清Python的模块、包和库

### 模块

一个.py文件就称之为一个模块（Module），一个模块里可能会包含很多函数，函数命名时，尽量不要与内置函数名字冲突。

**常见的内置函数见文章：**

Pandas的concat.py模块如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN26C8XxzMB3OtnE2YqWWk6YqCSgJ0CT5o7T06k46lK1lUX70WNl6OcDyia9UaeSdOBdZDYNme5Hgrjg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

里面包括3个函数和1个类

`注意`：

**系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块**。检查方法是在Python交互环境执行`import abc`，若成功则说明系统存在此模块。

### 包

包（Package）下有多个模块，如下为pandas 的reshape 包，里面包括多个.py 文件。

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN26C8XxzMB3OtnE2YqWWk6YqCK9BUkB84a9xS43IMqoSUQSXcYhSU0VOOW4uia1eR5lbG32awRRoWbw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

里面有一个.py文件比较特殊，也是每个包下必须包括的，它是`__init__.py`

`__init__.py`可以是空文件，在此处reshape包下的这个文件就是空的。当然，也可以有Python代码，因为`__init__.py`本身就是一个模块。模块`__init__.py`的模块名在此处就是`reshape`。



可以有多级层次的包结构。比如pandas的core包，含有如下的目录结构：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN26C8XxzMB3OtnE2YqWWk6Yqn3icAdt9Ehg6rPCKtNTCrQtWCw96EycLuuiarrFdLyWnZDzQickPmaQWw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



### 库

库是指具有相关功能模块的集合。这也是Python的一大特色之一，即具有强大的`标准库`、`第三方库`以及`自定义模块`。

**标准库**：python里那些自带的模块

**第三方库**：就是由其他的第三方机构，发布的具有特定功能的模块。比如2018年最受欢迎的几个库：TensorFlow、pandas、scikit-learn**、**PyTorch**、**Matplotlib**、Keras、**NumPy**、**SciPy**、**Apache MXNet**、**Theano**、**Bokeh**、**XGBoost**、**Gensim**、**Scrapy、**Caffe**

**自定义模块**：用户自己可以自行编写模块，然后使用。



导入模块与包都是通过import来导入的