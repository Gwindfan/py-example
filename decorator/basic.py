# -*- coding: utf-8 -*-
"""
名词解释：
装饰器其实也就是一个函数，一个用来包装函数的函数，返回一个修改之后的函数对象

装饰器类型可分为：类装饰器，函数装饰器
带参数与否又可分为：带参数的装饰器，不带参数的装饰器
嵌套与否又可分为：嵌套型，单一型

应用场景：
1. 注入参数（提供默认参数，生成参数）
2. 记录函数行为（日志、缓存、计时）
3. 预处理／后处理（配置上下文）
4. 修改调用时的上下文（线程异步或者并行，类方法）
"""
# 内置装饰器 @classmethod
# classmethod 做的只是函数转换，但是它却让foo这个名字另外出现了2次。
# 记得有一句话是：人类因懒惰而进步。Decorator的诞生，让foo少出现2次。
class C:
    def foo(cls, y):
        print "classmethod", cls, y
    # 函数对象被重新赋值
    foo = classmethod(foo)

# 改写之后
class C:
    @classmethod
    def foo(cls, y):
        print "classmethod", cls, y



"""
函数装饰器，不带参数，单层装饰
"""
def salesgirl(method):
    def serve(*args):
        print "Salesgirl:Hello, what do you want?", method.__name__
        result = method(*args)
        if result:
            print "Salesgirl: This shirt is 50$."
        else:
            print "Salesgirl: Well, how about trying another style?"
        return result
    return serve


@salesgirl
def try_this_shirt(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I:%d inches is just enough" %(size)
        return True


def try_this_shirt_no_at(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I:%d inches is just enough" %(size)
        return True


"""
函数装饰器，带参数，单层装饰
"""
def salesgirl_with_discount(discount):
    def expense(method):
        def serve(*args):
            print "Salesgirl:Hello, what do you want?", method.__name__
            result = method(*args)
            if result:
                print "Salesgirl: This shirt is 50$.As an old user, " \
                      "we promised to discount at %d%%" % discount
            else:
                print "Salesgirl: Well, how about trying another style?"
            return result
        return serve
    return expense


@salesgirl_with_discount(50)
def try_this_shirt_with_discount(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I:%d inches is just enough" %(size)
        return True


"""
类装饰器，不带参数，单层装饰
"""
# 相比函数装饰器，具有灵活度大，高内聚、封装性等优点
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')


def bar_neat():
    print ('neat bar')


"""
类装饰器，带参数，单层装饰
"""
# TBD


"""
在类中定义装饰器，不带参数，单层装饰
"""
from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a = A()
@a.decorator1
def spam():
    pass
# As a class method
@A.decorator2
def grok():
    pass


if __name__ == '__main__':
    c_obj = C()
    c_obj.foo('C object say Hello!')
    C.foo('Class C say Hello.')
    print '> 1 ', "-" * 60
    # 1） 函数装饰器，不带参数
    result = try_this_shirt(38)
    print "Mum:do you want to buy this?", result
    # 装饰效果等同如下
    print salesgirl(try_this_shirt_no_at)(38)
    # 由外向内拆解
    print salesgirl(try_this_shirt_no_at)
    print '> 2 ', "-" * 60

    # 2） 函数装饰器，带参数
    result = try_this_shirt_with_discount(38)
    print "Mum:do you want to buy this?", result
    # 装饰效果等同如下
    print salesgirl_with_discount(50)(try_this_shirt_no_at)(38)
    # 由外向内拆解
    print salesgirl_with_discount(50)
    print salesgirl_with_discount(50)(try_this_shirt_no_at)
    print '> 3 ', "-" * 60

    # 3） 类装饰器，不带参数，单层装饰
    bar()
    # 装饰效果等同如下
    Foo(bar_neat)()
    print '> 4 ', "-" * 60

    # 4） 类装饰器，带参数，单层装饰
    # TBD

    print '> 5 ', "-" * 60
    # 5） 在类中类装饰器，带参数，单层装饰
    spam()
    grok()



