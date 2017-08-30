#-*-coding:utf-8 -*-
def d1(F):
    print('d1')
    return lambda: 'X' + F()
def d2(F):
    print('d2')
    return lambda: 'Y' + F()
def d3(F):
    print('d3')
    return lambda: 'Z' + F()

@d1
@d2
@d3
def func():
    return 'foo'

def func_no_decorator():
    return 'bar'

"""
以下两种方式等价
"""
print(func())
print(d1(d2(d3(func_no_decorator)))())
"""
d3(func_no_decorator) return anonymous function to d2
d2(d3(func_no_decorator)) return anonymous function to d1
d1(d2(d3(func_no_decorator))) return anonymous function to caller
# 结论
- 函数／方法装饰器原则上返回function
- 装饰顺序，由内向外
- func_no_decorator 不断被加装饰，但只在最后执行一次
"""

func = func(*args, **kwargs)

func()
