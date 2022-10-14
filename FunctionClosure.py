def collection():
    lst = []
    def add_value(value):
        lst.append(value)
        return lst
    return add_value

def foo(x, y):
    def bar():
        nonlocal y
        x = 3
        y *= 5

    bar()    
    return x, y

print(foo(4, 5))