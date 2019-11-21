批量修改文件后缀

本例子使用Python的`os`模块和 `argparse`模块，将工作目录`work_dir`下所有后缀名为`old_ext`的文件修改为后缀名为`new_ext`

通过本例子，大家将会大概清楚`argparse`模块的主要用法。

### 1 导入模块

```
import argparse
import os
```

### 2 定义脚本参数

```python
def get_parser():
    parser = argparse.ArgumentParser(
        description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar='OLD_EXT',
                        type=str, nargs=1, help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT',
                        type=str, nargs=1, help='新的后缀')
    return parser
```

### 3 后缀批量重命名

```python
def batch_rename(work_dir, old_ext, new_ext):
    """
    传递当前目录，原来后缀名，新的后缀名后，批量重命名后缀
    """
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    print(os.listdir(work_dir))
```

### 4 实现main函数

```python
def main():
    """
    main函数
    """
    # 命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())
    # 从命令行参数中依次解析出参数
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)
```

如果使用Pycharm，直接在configuration界面配置即可，如果使用vs code，可在launch.json文件提前设置好参数：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: batch_file_rename",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "./a",
                "py",
                "txt"
            ]
        }
    ]
}
```

### 5 直接调用

```python
if __name__ == '__main__':
    main()
```



如果提前设置好了参数，则直接执行 batch_file_rename.py

如果未设置三个参数，需要在命令行这么传入：

```
batch_file_rename.py a py txt
```



