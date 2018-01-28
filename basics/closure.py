from functools import reduce

"""
sum
"""
def sum(mylist):
    return reduce(lambda x,y:x+y,mylist)

"""
lazy sum
"""
def lazy_sum(mylist):
    def sum():
        return reduce(lambda x, y: x + y, mylist)
    return sum


print(sum([1,3,5,7]))
#16

mysum = lazy_sum([1,3,5,7])
print(mysum)
#<function lazy_sum.<locals>.sum at 0x7f42c4166c80>
print(mysum())
#16

"""
lazy sum
"""
def lazy_sum2(mylist):
    tmp=10
    def sum():
        return reduce(lambda x, y: x + y, mylist)
    return sum,tmp


sumfun,tmp = lazy_sum2([1,3,5,7])
print(sumfun())
#16
print(tmp)
#10
