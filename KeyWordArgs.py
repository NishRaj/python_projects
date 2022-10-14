from operator import contains


def sum_items (a, b, c):
    print (a,b,c)
    return a + b + c

args = [1,2,3]
x = sum_items(*args)
print (x)

kwargs = {"a":5, "c":7, "b":3}
y = sum_items(**kwargs)
print(y)
print(*[1, 2, 3, 4], **{'end': "|", 'sep': "*"})
print (1,2,3,4, end= "|" , sep = '&')

def get_args_and_kwargs(*args, **kwargs):
    if len(args) + len(kwargs.keys()) > 3:
        if "num" in kwargs.keys() and kwargs.get("num") > 5:
            return True
    return False

args = ["a", [2]]
kwargs = {"num": 6}
print(get_args_and_kwargs(*args, **kwargs))
