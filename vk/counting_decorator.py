def counter(call_limit):
    def decorator(function):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            if wrapper.count > call_limit:
                raise Exception("Too many calls.")
            return function(*args, **kwargs)

        wrapper.count = 0
        return wrapper
    return decorator


@counter(call_limit=5)
def print_hello():
    print("hello")


for _ in range(10):
    print_hello()