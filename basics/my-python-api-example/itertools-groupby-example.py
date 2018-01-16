"""
example:
1 sorted by lambda
2 groupby
"""
from itertools import groupby

data =[("qaz",100),("wsx",92),("edc",87),("wsx",66),("ed",56),("wsx",43)]

groups = []
uniquekeys = []

data = sorted(data, key=lambda  r:r[0])

for k, g in groupby(data, lambda  r:r[0]):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)


print("end")
