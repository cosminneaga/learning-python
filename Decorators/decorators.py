# decorators are possible because functions are acting like variables
from textwrap import wrap


def hello(func):
    func()


def greet():
    print('still here')


hello(greet)


# HOC - Higher Order Function
# a HOC is a function that accepts another function as a parameter / return another function
def greet(func):  # higher order function
    func()


def greet():  # higher order function
    def func():
        return 5
    return func


# decorator
def my_decorator(func):
    def wrap_func():
        print('***')
        func()
        print('***')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('see ya')


hello()
bye()


# hello2 = my_decorator(hello)
# hello2()

# my_decorator(hello)()


# DECORATOR WITH PARAMS
def my_dec_params(func):
    def inner(x):
        print('###')
        func(x)
        print('###')
    return inner


@my_dec_params
def with_param(greeting):
    print(greeting)


with_param('hello there boy')


# DECORATOR WITH MULTI PARAMS
def my_dec_multi_params(func):
    def inner(*args, **kwargs):
        print('###')
        func(*args, *kwargs)
        print('###')
    return inner


@my_dec_multi_params
def with_param(greeting, emoji=':)'):
    print(greeting, emoji)


with_param('hello there boy', ':)))')
with_param('hello there boy')
