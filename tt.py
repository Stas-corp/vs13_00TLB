import timeit
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        total_time = end_time - start_time
        print(f'Func {func.__name__} worked {total_time} seconds!')
        return result
    return wrapper

@timing_decorator
def three_seconds_func():
    for i in range(1,4):
        print(i)
        time.sleep(1)


# three_seconds_func()
