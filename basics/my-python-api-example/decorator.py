import time
"""
log function to add func
"""

def log(func):
    def wrapper():
        print('call %s():' % func.__name__)
        return func()
    return wrapper



"""
decorator log
"""

@log
def now():
    timenow = time.localtime(time.time())
    return time.strftime('%Y-%m-%d %H:%M:%S',timenow)

print(now())