"""
map
"""


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(list(map(char2num,"24678")))


"""
reduce
"""


def fn(x, y):
    return x * 10 + y


from functools import reduce


r = reduce(fn, [1, 3, 5, 7, 9])
print(r)





"""
map-reduce
"""


def str2num(s):
    return reduce(fn, map(char2num, s))

print(str2num('213579'))



"""
filter
"""


def isEven(n):
    return n % 2 == 0


print(list(filter(isEven, [1, 2, 4, 5, 6, 9, 10, 15])))


"""
sorted
"""


print(sorted(['jack', 'amily', 'tom', 'abama'], key=str.lower))


print(sorted(['jack', 'amily', 'tom', 'abama'], key=str.lower,reverse=True))
