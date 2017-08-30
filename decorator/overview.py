# -*- coding: utf-8 -*-

"""
装饰器类型可分为：类装饰器，函数装饰器
带参数与否又可分为：带参数的装饰器，不带参数的装饰器
嵌套与否又可分为：嵌套型，单一型
"""
# 内置装饰器 @classmethod
# classmethod做的只是函数转换，但是它却让foo这个名字另外出现了2次。
# 记得有一句话是：人类因懒惰而进步。Decorator的诞生，让foo少出现2次。
class C:
    def foo(cls, y):
        print "classmethod", cls, y
    foo = classmethod(foo)

# 改写之后
class C:
    @classmethod
    def foo(cls, y):
        print "classmethod", cls, y

if __name__ == '__main__':
    c_obj = C()
    c_obj.foo('C object say Hello!')
    C.foo('Class C say Hello.')
