# -*- coding: UTF-8 -*-
"""
闭包在装饰器场景的应用
"""
def counter(func):
    def incr():
        incr.count += 1
        print incr.count
        func()
    incr.count = 0
    print "count ++"
    return incr


from time import ctime


def before_call(f):
    def wrapped(*args, **kargs):
        print 'before calling, now is %s' % ctime()
        return f(*args, **kargs)
    return wrapped