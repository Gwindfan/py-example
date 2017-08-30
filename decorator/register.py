#Registering decorated objects to an API
registry = {}

def register(obj):
    registry[obj.__name__] = obj
    return obj

# spam = register(spam)
@register
def spam(x):
    return(x ** 2)

@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))