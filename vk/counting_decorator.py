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


if __name__ == '__main__':
    while True:
        print_hello()
