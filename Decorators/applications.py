from time import time


def performance(f):
    def inner(*args, **kwargs):
        t1 = time()
        result = f(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result
    return inner


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()
