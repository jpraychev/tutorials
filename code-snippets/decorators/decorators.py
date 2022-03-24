# Simple decorator that does nothing.
# Return decorated function with argument.
def decorator(f):

    def wrapper(inner_name):
        return f(inner_name)
    return wrapper

# General decorator that does nothing.
# Return decorated function with args and kwargs.
def general_decorator(f):

    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


@decorator
def get_name(name):
    return f'Hi, {name}'

if __name__ == '__main__':

    username = get_name('Jordan')
    print(username)

    
    

    

