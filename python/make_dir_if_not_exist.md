检查目录是否存在，不存在则创建。

### 1 导入模块

```
import os
```

### 2 创建目录

检查目录`newdir`是否存在于当前目录下，

不存在则创建；

存在则提示`MESSAGE`;

```
def make_dir_if_not_exist(newdir):
    MESSAGE = '文件已经存在'
    try:
        curdir = "."
        print('home= ' + curdir)
        if not os.path.exists(os.path.join(curdir, newdir)):
            # 如果不存在，创建它
            os.makedirs(os.path.join(curdir, newdir))
            print('创建成功')
        else:
            print(MESSAGE)
    except Exception as e:
        print(e)

```
调用
```
if __name__ == "__main__":
    make_dir_if_not_exist('testdir')
```