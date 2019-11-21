### 0 共用模块

模块名称：example_utils.py，里面包括三个函数，各自功能如下：

```python
import matplotlib.pyplot as plt

# 创建画图fig和axes
def setup_axes():
    fig, axes = plt.subplots(ncols=3, figsize=(6.5,3))
    for ax in fig.axes:
        ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(wspace=0, left=0, right=0.93)
    return fig, axes
# 图片标题
def title(fig, text, y=0.9):
    fig.suptitle(text, size=14, y=y, weight='semibold', x=0.98, ha='right',
                 bbox=dict(boxstyle='round', fc='floralwhite', ec='#8B7E66',
                           lw=2))
# 为数据添加文本注释
def label(ax, text, y=0):
    ax.annotate(text, xy=(0.5, 0.00), xycoords='axes fraction', ha='center',
                style='italic',
                bbox=dict(boxstyle='round', facecolor='floralwhite',
                          ec='#8B7E66'))
```



### 1 基本绘图

![1573699352403](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573699352403.png)

对应代码：

```python
import numpy as np
import matplotlib.pyplot as plt

import example_utils

x = np.linspace(0, 10, 100)

fig, axes = example_utils.setup_axes()
for ax in axes:
    ax.margins(y=0.10)

# 子图1 默认plot多条线，颜色系统分配
for i in range(1, 6):
    axes[0].plot(x, i * x)

# 子图2 展示线的不同linestyle
for i, ls in enumerate(['-', '--', ':', '-.']):
    axes[1].plot(x, np.cos(x) + i, linestyle=ls)

# 子图3 展示线的不同linestyle和marker
for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
    axes[2].plot(x, np.cos(x) + i * x, linestyle=ls, marker=mk, markevery=10)

# 设置标题
# example_utils.title(fig, '"ax.plot(x, y, ...)": Lines and/or markers', y=0.95)
# 保存图片
fig.savefig('plot_example.png', facecolor='none')
# 展示图片
plt.show()
```



###  2 散点图



![1573699993369](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573699993369.png)

对应代码：

```python
"""
散点图的基本用法
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils

# 随机生成数据
np.random.seed(1874)
x, y, z = np.random.normal(0, 1, (3, 100))
t = np.arctan2(y, x)
size = 50 * np.cos(2 * t)**2 + 10

fig, axes = example_utils.setup_axes()

# 子图1
axes[0].scatter(x, y, marker='o',  color='darkblue', facecolor='white', s=80)
example_utils.label(axes[0], 'scatter(x, y)')

# 子图2
axes[1].scatter(x, y, marker='s', color='darkblue', s=size)
example_utils.label(axes[1], 'scatter(x, y, s)')

# 子图3
axes[2].scatter(x, y, s=size, c=z,  cmap='gist_ncar')
example_utils.label(axes[2], 'scatter(x, y, s, c)')

# example_utils.title(fig, '"ax.scatter(...)": Colored/scaled markers',
#                     y=0.95)
fig.savefig('scatter_example.png', facecolor='none')

plt.show()
```



### 3 柱状图

![1573700241030](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573700241030.png)

对应代码：

```python
import numpy as np
import matplotlib.pyplot as plt

import example_utils


def main():
    fig, axes = example_utils.setup_axes()

    basic_bar(axes[0])
    tornado(axes[1])
    general(axes[2])

    # example_utils.title(fig, '"ax.bar(...)": Plot rectangles')
    fig.savefig('bar_example.png', facecolor='none')
    plt.show()

# 子图1
def basic_bar(ax):
    y = [1, 3, 4, 5.5, 3, 2]
    err = [0.2, 1, 2.5, 1, 1, 0.5]
    x = np.arange(len(y))
    ax.bar(x, y, yerr=err, color='lightblue', ecolor='black')
    ax.margins(0.05)
    ax.set_ylim(bottom=0)
    example_utils.label(ax, 'bar(x, y, yerr=e)')

# 子图2
def tornado(ax):
    y = np.arange(8)
    x1 = y + np.random.random(8) + 1
    x2 = y + 3 * np.random.random(8) + 1
    ax.barh(y, x1, color='lightblue')
    ax.barh(y, -x2, color='salmon')
    ax.margins(0.15)
    example_utils.label(ax, 'barh(x, y)')

# 子图3
def general(ax):
    num = 10
    left = np.random.randint(0, 10, num)
    bottom = np.random.randint(0, 10, num)
    width = np.random.random(num) + 0.5
    height = np.random.random(num) + 0.5
    ax.bar(left, height, width, bottom, color='salmon')
    ax.margins(0.15)
    example_utils.label(ax, 'bar(l, h, w, b)')


main()
```



### 4 填充画图

![1573700535446](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573700535446.png)

对应代码：

```python
"""
fill函数的各种用法
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils


# -- 产生数据 ----------------------


def stackplot_data():
    x = np.linspace(0, 10, 100)
    y = np.random.normal(0, 1, (5, 100))
    y = y.cumsum(axis=1)
    y -= y.min(axis=0, keepdims=True)
    return x, y


def sin_data():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y2 = np.cos(x)
    return x, y, y2


def fill_data():
    t = np.linspace(0, 2*np.pi, 100)
    r = np.random.normal(0, 1, 100).cumsum()
    r -= r.min()
    return r * np.cos(t), r * np.sin(t)


def fill_example(ax):
    # fill一个多边形区域
    x, y = fill_data()
    ax.fill(x, y, color='lightblue')
    ax.margins(0.1)
    example_utils.label(ax, 'fill')


def fill_between_example(ax):
    # 两条线间填充
    x, y1, y2 = sin_data()

    # fill_between的最常用法1
    err = np.random.rand(x.size)**2 + 0.1
    y = 0.7 * x + 2
    ax.fill_between(x, y + err, y - err, color='orange')

    # 最常用法2:两条曲线相交区域对应不同填充色
    ax.fill_between(x, y1, y2, where=y1 > y2, color='lightblue')
    ax.fill_between(x, y1, y2, where=y1 < y2, color='forestgreen')

    # 最常用法3
    ax.fill_betweenx(x, -y1, where=y1 > 0, color='red', alpha=0.5)
    ax.fill_betweenx(x, -y1, where=y1 < 0, color='blue', alpha=0.5)

    ax.margins(0.15)
    example_utils.label(ax, 'fill_between/x')


def stackplot_example(ax):
    # Stackplot就是多次调用 ax.fill_between
    x, y = stackplot_data()
    ax.stackplot(x, y.cumsum(axis=0), alpha=0.5)
    example_utils.label(ax, 'stackplot')


def main():
    fig, axes = example_utils.setup_axes()

    fill_example(axes[0])
    fill_between_example(axes[1])
    stackplot_example(axes[2])

    # example_utils.title(fig, 'fill/fill_between/stackplot: Filled polygons',
    #                     y=0.95)
    fig.savefig('fill_example.png', facecolor='none')
    plt.show()


main()
```



### 5 imshow

![1573710321269](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573710321269.png)

对应代码：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data
from mpl_toolkits import axes_grid1

import example_utils


def main():
    fig, axes = setup_axes()
    plot(axes, *load_data())
    # example_utils.title(fig, '"ax.imshow(data, ...)": Colormapped or RGB arrays')
    fig.savefig('imshow_example.png', facecolor='none')
    plt.show()


def plot(axes, img_data, scalar_data, ny):

    # 默认线性插值
    axes[0].imshow(scalar_data, cmap='gist_earth', extent=[0, ny, ny, 0])

    # 最近邻插值
    axes[1].imshow(scalar_data, cmap='gist_earth', interpolation='nearest',
                   extent=[0, ny, ny, 0])

    # 展示RGB/RGBA数据
    axes[2].imshow(img_data)


def load_data():
    img_data = plt.imread(get_sample_data('5.png'))
    ny, nx, nbands = img_data.shape
    scalar_data = np.load(get_sample_data('bivariate_normal.npy'))
    return img_data, scalar_data, ny


def setup_axes():
    fig = plt.figure(figsize=(6, 3))
    axes = axes_grid1.ImageGrid(fig, [0, 0, .93, 1], (1, 3), axes_pad=0)

    for ax in axes:
        ax.set(xticks=[], yticks=[])
    return fig, axes


main()
```



### 6 pcolor



![1573710387302](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573710387302.png)

对应代码：

```python
"""
pcolor/pcolormesh的基本用法
记住一点：假如数据在矩形区域内建议使用imshow，这样速度更快。此例子展示imshow不能使用的场景

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data

import example_utils

# 拿到数据 ...
z = np.load(get_sample_data('./bivariate_normal.npy'))
ny, nx = z.shape
y, x = np.mgrid[:ny, :nx]
y = (y - y.mean()) * (x + 10)**2

mask = (z > -0.1) & (z < 0.1)
z2 = np.ma.masked_where(mask, z)

fig, axes = example_utils.setup_axes()

# pcolor 或 pcolormesh 都可，后者效率更高
axes[0].pcolor(x, y, z, cmap='gist_earth')
example_utils.label(axes[0], 'either')

# pcolor和pcolormesh的不同展示
# 使用pcolor
axes[1].pcolor(x, y, z2, cmap='gist_earth', edgecolor='black')
example_utils.label(axes[1], 'pcolor(x,y,z)')

# 使用pcolormesh
axes[2].pcolormesh(x, y, z2, cmap='gist_earth', edgecolor='black', lw=0.5,
                   antialiased=True)
example_utils.label(axes[2], 'pcolormesh(x,y,z)')

#example_utils.title(fig, 'pcolor/pcolormesh: Colormapped 2D arrays')
fig.savefig('pcolor_example.png', facecolor='none')

plt.show()

```

### 7 contour



![1573710525645](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573710525645.png)



对应代码：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data

import example_utils

z = np.load(get_sample_data('bivariate_normal.npy'))

fig, axes = example_utils.setup_axes()

axes[0].contour(z, cmap='gist_earth')
example_utils.label(axes[0], 'contour')

axes[1].contourf(z, cmap='gist_earth')
example_utils.label(axes[1], 'contourf')

axes[2].contourf(z, cmap='gist_earth')
cont = axes[2].contour(z, colors='black')
axes[2].clabel(cont, fontsize=6)
example_utils.label(axes[2], 'contourf + contour\n + clabel')

# example_utils.title(fig, '"contour, contourf, clabel": Contour/label 2D data',
#                     y=0.96)
fig.savefig('contour_example.png', facecolor='none')

plt.show()

```



### 8 向量场

![1573710732713](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573710732713.png)

对应代码：

```python
import matplotlib.pyplot as plt
import numpy as np

import example_utils

# Generate data
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
xi, yi = np.meshgrid(x, y)
z = (1 - xi / 2 + xi**5 + yi**3) * np.exp(-xi**2 - yi**2)
dy, dx = np.gradient(z)
mag = np.hypot(dx, dy)

fig, axes = example_utils.setup_axes()

# 单箭头
axes[0].arrow(0, 0, -0.5, 0.5, width=0.005, color='black')
axes[0].axis([-1, 1, -1, 1])
example_utils.label(axes[0], 'arrow(x, y, dx, dy)')

# ax.quiver
ds = np.s_[::16, ::16]  # Downsample our array a bit...
axes[1].quiver(xi[ds], yi[ds], dx[ds], dy[ds], z[ds], cmap='gist_earth',
               width=0.01, scale=0.25, pivot='middle')
axes[1].axis('tight')
example_utils.label(axes[1], 'quiver(x, y, dx, dy)')

# ax.streamplot
# 宽度和颜色变化
lw = 2 * (mag - mag.min()) / mag.ptp() + 0.2
axes[2].streamplot(xi, yi, dx, dy, color=z, density=1.5, linewidth=lw,
                   cmap='gist_earth')
example_utils.label(axes[2], 'streamplot(x, y, dx, dy)')

# example_utils.title(fig, '"arrow/quiver/streamplot": Vector fields', y=0.96)
# fig.savefig('vector_example.png', facecolor='none')

plt.show()
```



### 9 数据分布图



![1573711009411](C:\Users\guozhen3\AppData\Roaming\Typora\typora-user-images\1573711009411.png)

对应代码：

```python
"""
Matplotlib 提供许多专业的绘制统计学相关的图函数

更多统计学相关图可使用 Seaborn 库，它基于Matplotlib编写。 
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils


def main():
    colors = ['cyan', 'red', 'blue', 'green', 'purple']
    dists = generate_data()

    fig, axes = example_utils.setup_axes()
    hist(axes[0], dists, colors)
    boxplot(axes[1], dists, colors)
    violinplot(axes[2], dists, colors)

    # example_utils.title(fig, 'hist/boxplot/violinplot: Statistical plotting',
    #                     y=0.9)
    fig.savefig('statistical_example.png', facecolor='none')

    plt.show()


def generate_data():
    means = [0, -1, 2.5, 4.3, -3.6]
    sigmas = [1.2, 5, 3, 1.5, 2]
    # 每一个分布的样本个数
    nums = [150, 1000, 100, 200, 500]

    dists = [np.random.normal(*args) for args in zip(means, sigmas, nums)]
    return dists

# 频率分布直方图
def hist(ax, dists, colors):
    ax.set_color_cycle(colors)
    for dist in dists:
        ax.hist(dist, bins=20, density=True, edgecolor='none', alpha=0.5)

    ax.margins(y=0.05)
    ax.set_ylim(bottom=0)

    example_utils.label(ax, 'ax.hist(dists)')

# 箱型图
def boxplot(ax, dists, colors):
    result = ax.boxplot(dists, patch_artist=True, notch=True, vert=False)

    for box, color in zip(result['boxes'], colors):
        box.set(facecolor=color, alpha=0.5)
    for item in ['whiskers', 'caps', 'medians']:
        plt.setp(result[item], color='gray', linewidth=1.5)
    plt.setp(result['fliers'], markeredgecolor='gray', markeredgewidth=1.5)
    plt.setp(result['medians'], color='black')

    ax.margins(0.05)
    ax.set(yticks=[], ylim=[0, 6])

    example_utils.label(ax, 'ax.boxplot(dists)')

#小提琴图
def violinplot(ax, dists, colors):
    result = ax.violinplot(dists, vert=False, showmedians=True)
    for body, color in zip(result['bodies'], colors):
        body.set(facecolor=color, alpha=0.5)
    for item in ['cbars', 'cmaxes', 'cmins', 'cmedians']:
        plt.setp(result[item], edgecolor='gray', linewidth=1.5)
    plt.setp(result['cmedians'], edgecolor='black')

    ax.margins(0.05)
    ax.set(ylim=[0, 6])

    example_utils.label(ax, 'ax.violinplot(dists)')


main()

```



