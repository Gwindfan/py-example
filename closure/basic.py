# -*- coding: UTF-8 -*-

"""
闭包 = 函数块 + 定义函数时的环境[变量]
函数块: addy
环境: x
"""
def addx(x):
    def addy(y):
        return x + y
    return addy

sum = addx(8)   # sum = 8 + y
print "type of sum: %s, value of sum: %s" % (type(sum), sum)
print "func name:", sum.__name__
print '{}'.format(sum(10))


"""
闭包与内部函数
"""
def test(a):
    def add():                                # 没用引用外部函数的参数
        return "it's a callable %s" % a       # 直接在内部函数使用外部函数的参数
    return add                                # 返回内部函数本身，不返回内部函数调用!

a1 = test(1)
print "type of a1: %s, value of a1: %s" % (type(a1), a1())
print "test(1)(): ", test(1)()


"""
函数是一个对象，所以可以作为某个函数的返回结果
"""
def line_conf():
    def line(x):
        return 2 * x + 1
    return line       # return a function object

my_line = line_conf()
print "my_line: ", my_line(5)


"""
如果line()的定义中引用了外部的变量
"""
def line_conf():
    b = 15
    # line定义的隶属程序块中引用了高层级的变量b，但b信息存在于line的定义之外 (b的定义并不在line的隶属程序块中)。
    # 我们称 b 为 line 的"环境变量"
    # 事实上，line 作为 line_conf的返回值时，line中已经包括b的取值(尽管b并不隶属于line)
    def line(x):
        return 2 * x + b
    return line       # return a function object

b = 5   # 不会覆盖 line 的环境变量 b
my_line = line_conf()
print "引用外部变量后 my_line:", my_line(5)


"""
所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中
"""
def line_conf():
    b = 15
    def line(x):
        return 2 * x + b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line.func_closure)     # or my_line.__closure__
print(my_line.func_closure[0].cell_contents)


"""
这个例子中，函数line与环境变量a,b构成闭包。在创建闭包的时候，我们通过line_conf的参数a,b说明了这两个环境变量的取值，
这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。我们只需要变换参数a,b，就可以获得不同的直线表达函数。
由此，我们可以看到，闭包也具有提高代码可复用性的作用。
"""
def line_conf(a, b):
    def line(x):
        return a * x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))


"""
总结
1.一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。闭包是函数式编程的重要的语法结构
简单说，就是套嵌的 def，第二层的 def 函数逻辑是可以直接访问上层的局部作用域的变量
2.函数是一个对象，所以可以作为某个函数的返回结果
3.所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中
3.闭包可提高代码复用性
4.闭包有效的减少了函数所需定义的参数数目
5.应用于并行运算, 函数式编程, 典型的应用为装饰器
"""