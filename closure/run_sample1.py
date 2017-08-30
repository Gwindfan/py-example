from closure_sample1 import counter, before_call

@counter
def test():
    pass

for i in range(1, 5):
    test()


@before_call
def test(name):
    print 'hello, %s' % (name)

test("lucky")