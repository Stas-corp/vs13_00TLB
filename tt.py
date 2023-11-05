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

print(2%3)

def all_sub_lists(lst):
    sub_lists = [[]]  # Починаємо з порожнього підсписку

    for i in range(len(lst)):
        sub_lists.append([lst[i]])

    for i in range(len(lst)-1):
        sub_lists.append(lst[i:i+2])

    for i in range(len(lst)-2):
        sub_lists.append(lst[i:i+3])  

    for i in range(len(lst)-3):
        sub_lists.append(lst[i:i+4])  

    return sub_lists

# Приклад використання
my_list = [4, 6, 1, 3]
result = all_sub_lists(my_list)
print(result)
