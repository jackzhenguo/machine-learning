### JavaScript 快速入门



别问做算法和数据分析的，怎么还学js. 工作了需要啥都得学，还得快。这就是互联网，适者生存，劣者淘汰。



我在几年前接触过一些js，那时对this, that混用觉得很烦, promise用起来不是很清。不过，学习是一件奇怪的事，现在再看，发现对这些点又有了新的理解。



这是一个精简的小白入门js的课程总结



### 1 js代码放哪里执行？

js代码可以直接嵌套在html中，通常部署在head中：

```javascript
<head>
  <script>
  	alert('Hello, world');
  </script>
</head>
```

js的代码末尾可不加分号，但是最好加上，这样chrome内核解析时不会出现意味错误。

当js代码变长时，直接放在head中，会很臃肿，也不符合模块要分离的要求，维护不方便。单独放到一个.js文件中会很好，然后通过 `<script src="/static/js/jquery-min.js"></script>`引入这个文件。

一个最简单的例子，我的demo.js文件：

```javascript
function demoFun(){
    alert('hello world')
}

demoFun();

```

我的html文件，使用script标签的src属性引用demo.js文件。

```javascript
<html>
<head>
  <script src="demo.js"></script>
</head>
<body>
  ...
</body>
</html>
```



编写js代码的IDE,推荐 vs code. 完成一个Html后，立即可以放入浏览器执行。如果html涉及到联网等，需要一个web服务器部署上。



### 2 核心语法

1. 最好语句后加上分号
2. 不区分整数和浮点数，都为Number，其他类型：字符串，布尔型，数组(元素类型不区分)，map, set.
3. zglg = {name: 'xiaoming', age:27} ，这是js中定义一个对象或者类的方法
4. var 关键字表示是变量，类型待定，建议禁止省略
5. if, while, for和 java一致
6. 需要重点说明，函数是js中的头等公民，函数完全可以当变量用，抽象能力抽强。*下面总结核心知识*。
7. js中变量作用域，函数体内声明的变量只能在体内使用，不在任何一个函数体内的变量具有全局作用域。值得注意：函数体内声明的变量都会提到函数体的开头部分。
8. js的全局变量，也无法逃出window变量，它才是全局的根变量
9. 一个函数被绑定在对象内，就成为"方法" ，*下面总结核心知识*。
10. 如果A函数的参数也是函数，A函数就是高阶函数
11. ES6新增的箭头函数，this作用域指向更加符合我们的预期
12. 闭包和generator与python中的原理和用法很相似，新手直接认为一样就行
13. js中常用的标准对象：Date, RegExp, Json



### 3 头等公民函数

function关键字指明是一个函数，

```javascript
function getReluResult(){
    if(this.inputval<0){
        return 0.;
    }
    else{
        return this.inputval;
    }
}
```

让getReluResult成为方法，

```javascript
var rnn ={
    name:'rnn object',
    inputval: -1.32,
    relu:getReluResult
}
```

这样relu 立即称为rnn对象的方法，调用：

```javascript
rnn.relu()
```

reduce高阶函数，

```javascript
var lis = [1,4,-9,3,6,5-3];
lis.reduce((x,y)=> x+y);//reduce是js中的一个内置高阶函数
```



高阶函数为什么说它是一种高阶抽象？ 数组求和可以这么写：

```javascript
function sum(list){
    var ret = 0.;
    for(var i=0; i<list.length;i++){
        ret+=list[i];
    }
    return ret;
}
```

但是，如果求连乘积呢？可能你又得写一个函数，无法复用sum这种框架，如果抽象出f 函数，作为这个框架的参数，情况可能好些，

```javascript
function myreduce(f,list){
    if(list.length<2){
        return 'length < 2';
    }
    var temp = f(list[0],list[1])
    for(var i=2; i<list.length;i++){
        temp = f(temp,list[i]);
    }
    return temp;
}
```

这么调用：

```javascript
myreduce((x,y)=>x+y, list); //求和
myreduce((x,y)=>x*y, list); //求乘积
```

你看，无论怎么操作，我们都能套用myreduce这个函数框架，只需抽象出一个函数f 作为其参数。







