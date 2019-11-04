### 1 两个时间模块

python与时间相关的内置模块有: time 和 datetime.  其中，time模块提供各种操作时间的函数，datetime模块定义了如下几个类型：

- datetime.date：日期类，常用的属性有 year, month, day; 
- datetime.time：时间类，常用的属性有 hour, minute, second, microsecond；
- datetime.datetime：日期时间；
- datetime.timedelta：时间间隔，即两个时间点相差长度；
- datetime.tzinfo：与时区有关的抽象基类

### 2 时间表达方式

常用的有以下几种，总结。

时间戳

第一，时间戳的方式. 相对于1970.1.1 00:00:00, 以秒计算的偏移量, 时间戳是惟一的，如：138267830.87.  *我看这是网上或大部分博客对时间戳的定义，不过这是不够严谨的，需要考虑所处的时区，此处衡量的时区为UTC(世界标准时间)*

为了验证以上逻辑，我们写一个例子：
```
dtime3 = datetime.datetime(1970,1,1)
dtime3.timestamp() 
```
预期输出为 0， 因为是相对于1970.1.1 00:00:00的偏移吗，所以预期为0. 可是在本地(中国)输出的时间戳是：-28800.0秒，也就是-8小时，也就是比预期的晚了8个小时。

问题就是处在没有考虑时区上。原定义是相对于UTC时区的，但是我们的datetime.datetime(1970,1,1) 因为没有显示的设置时区，程序会默认按照本地时区计算。

进一步修正：

```python
dtime2 = datetime.datetime(1970,1,1,tzinfo=timezone.utc)  
dtime2.timestamp() 
```

输出为 0.0

在此，我们为tzinfo设置时区为UTC，得到了最严格的时间戳的标准值定义。tzinfo 是datetime模块的抽象基类，上面提到过。

```python
class tzinfo(builtins.object)
 |  Abstract base class for time zone info objects.
```
python内置模块timezone是对tzinfo的一个标准实现类，如cpython中的源码(参考文件：*cpython/Lib/datetime.py*)
```
class timezone(tzinfo):
    __slots__ = '_offset', '_name'

```

时间数组

第二，以数组的形式表示即(struct_time). 共有九个元素分别表示。同样，同一个时间戳的struct_time会因为时区不同，而不同。

如：time.struct_time(tm_year=2013, tm_mon=10, tm_mday=25, tm_hour=13, tm_min=21, tm_sec=33, tm_wday=4, tm_yday=298, tm_isdst=0)

前面几个字面意思很清晰，后面四个：

tm_wday：(0-6, Monday is 0)

tm_yday：(day in the year, 1-366)

tm_isdst：(-1, 0 or 1)  0：普通  1：DST夏令时比正常的早一个小时  -1：根据当前时区

* 还有一种只能算作一种显示型式，字符串，如：2013-10-25 13:29:39.543000


可读性最强

最后一种是一种显示型式，也是我们最直观的显示方式，平时使用较多的日期和时间的表达方式。字符串，如：2013-10-25 13:29:39.543000


### 3 aware 和 naive 时间

这些在第2章节，其实我们已经有所涉及，简单来说aware日期时间会考虑时区等的因素，比如tzinfo设置为UTC后，时间戳就会相对于UTC求一个偏移。而，naive时间日期无法用户设置时区，选用哪个时区完全靠执行代码的系统决定，官方解释：

> Whether a **naive** object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program

### 4 常用API

理解了上面说的这些日期和时间的基本概念后，再用起来就不会掉坑了，下面总结一些常用的吧，网上这方面的一搜一大把，我尽量整理一个标准版本吧。

整理思路就是按照三种时间日期的表达格式，再有三种表达的相互转换。

#### 4.1 time 模块
```
import time

time.time()#获得自己所在时区的当前时间的时间戳
1382679270.196

time.clock()#3.8要废弃了
改为使用 time.process_time() 计算cpu的运行时间

time.mktime((2019,5,14, 0,0,0, 0,0,0))#利用mktime函数创建一个时间戳
1557763200.0, 注意必须是9元组
```

##### 4.1.1 **封装格式函数**
提炼使用较多的函数，将任意格式的时间日期字符串，转化为我们熟悉的时间日期格式

```
def toMyFormat(inputstr, inputfmt = "%a %b %d %H:%M:%S %Y"):
	tstruct = time.strptime(inputstr ,inputfmt) #转化为struct_time         return time.strftime("%Y-%m-%d %H:%M:%S", tstruct) #转化为定制的格式  
```


##### 4.1.2 **时间戳转struct_time**
```
In [91]: a = time.time() #时间戳                                                                            
Out[92]: 1557819720.375314

In [94]: time.gmtime(a) # 用UTC表达的struct_time                                                                         
Out[94]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=7, tm_min=42, tm_sec=0, tm_wday=1, tm_yday=134, tm_isdst=0)

In [96]: time.localtime() # 用localtime表达的struct_time                                                               
Out[96]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=15, tm_min=43, tm_sec=27, tm_wday=1, tm_yday=134, tm_isdst=0)

```

##### 4.1.3 **时间戳转字符串**

```
In [100]: time.ctime(a) # 时间戳转字符串格式(本地时区表达)                                                                    
Out[100]: 'Tue May 14 15:42:00 2019'

```

这个时间格式不是我们想要的，直接使用上面提到的封装后的日期转化函数toMyFormat 即可。


##### 4.1.4 **struct_time转字符串**
```
In [122]: import time                                                                      

In [123]: a = time.localtime()                                                             

In [124]: a                                                                                
Out[124]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=16, tm_min=36, tm_sec=30, tm_wday=1, tm_yday=134, tm_isdst=0)

In [125]: b = time.asctime(a) # struct_time转时间戳                                                             

In [126]: b                                                                                
Out[126]: 'Tue May 14 16:36:30 2019'

In [127]: toMyFormat(b)                                                                  
Out[127]: '2019-05-14 16:36:30'

```

##### 4.1.5 **struct_time转时间戳**
```
In [132]: a = time.gmtime()                                                                

In [133]: a                                                                                
Out[133]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=8, tm_min=38, tm_sec=55, tm_wday=1, tm_yday=134, tm_isdst=0)

In [136]: time.mktime(a) #stuct_time转为时间戳                                                                  
Out[136]: 1557794335.0


```

##### 4.1.6 **字符串转struct_time**
```
In [146]: b                                                                                
Out[146]: 'Tue May 14 16:44:16 2019'

In [147]: time.strptime(b,'%a %b %d %H:%M:%S %Y') #str格式转struct_time                                        
Out[147]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=16, tm_min=44, tm_sec=16, tm_wday=1, tm_yday=134, tm_isdst=-1)

```

##### 4.1.7 **字符串转时间戳**
字符串转为strct_time，然后使用time.mktime(a)转化为时间戳。




#### 4.2 **datetime模块**
datetime模块包括datetime类，date类，time类，timedelta类，tzinfo类。

##### 4.2.1 **datetime**

```
from datetime import *
date.today()*获取今天的日期：datetime.date(2019, 5, 14)

datetime.today()#获取今天的日期和时间：datetime.datetime(2019, 5, 14, 12, 36, 33, 382046)

dtime = datetime.now()# 获取当前的日期和时间，类似于 today()

datetime.datetime(2019, 5, 14, 12, 36, 33, 322000) # 构造出一个datetime实例

dtime.date()                                                                     
Out[154]: datetime.date(2019, 5, 14) # date类

dtime.time()                                                                     
Out[155]: datetime.time(16, 49, 57, 399473) #注意此time类不是time模块

In [157]: dtime.day                                                                        
Out[157]: 14

In [158]: dtime.month                                                                      
Out[158]: 5
	
```

##### 4.2.2 **date**
一个date对象表示年月日的组合，使用的日历为Gregorian。上面常用到的属性：
```
In [199]: a                                                                                
Out[199]: datetime.datetime(2019, 5, 14, 17, 1, 35, 804091)

In [200]: ad = a.date                                                                      
In [202]: ad = a.date()                                                                    
In [203]: ad                                                                               
Out[203]: datetime.date(2019, 5, 14)

In [204]: ad.timetuple() # 转为time模块中的struct_time类                                                                  
Out[204]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=14, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=134, tm_isdst=-1)

In [205]: ad.weekday() #返回周几，Monday为0，Sunday为6                                                                 
Out[205]: 1

In [206]: ad.isoweekday()   #返回周几，Monday为1，Sunday为7                                                           
Out[206]: 2

In [218]: ad                                                                               
Out[218]: datetime.date(2019, 5, 14)

In [219]: ad.ctime() # 转化为时间的字符串                                                                        
Out[219]: 'Tue May 14 00:00:00 2019'

In [220]: ad.strftime("%Y-%m-%d") #按照指定格式转化                                                         
Out[220]: '2019-05-14'

In [222]: ad.strftime("%Y-%m-%d %H:%M:%S")                                                 
Out[222]: '2019-05-14 00:00:00'


```

##### 4.2.3  **time**

时间对象代表本地时间，不含年月日，可以由 tzinfo 调整。注意与time模块区分，此time为datetime模块下的类。



##### 4.2.4 **timedelta**

timedelta对象代表两个日期或时间的间隔，是一个周期。

timedelta类的定义如下：
```
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

timedelta类实例支持加减乘除等操作，如下：

```
In [189]: a = datetime.today()                                                             

In [190]: a                                                                                
Out[190]: datetime.datetime(2019, 5, 14, 17, 1, 35, 804091)

In [191]: b = datetime(2019,5,15,18)                                                       

In [192]: b                                                                                
Out[192]: datetime.datetime(2019, 5, 15, 18, 0)

In [193]: b - a                                                                            
Out[193]: datetime.timedelta(days=1, seconds=3504, microseconds=195909)

```