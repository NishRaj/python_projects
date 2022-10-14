def add_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) +1
        return result
    
    return wrapper



#print(add_value(1,2,3))

def print_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        #return result
    return wrapper

@print_return_value
def add_value(x,y,z):
    return x+y+z

add_value(1,2,3)