from yaml import load
from mykonos.orcestrator import Orcestrator


with open('test/setting.yaml') as f:
    data = load(f)

data
data

orc = Orcestrator(data)
result = orc.device_info()
result

orc.turn_on_screen()


def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf1

print(nf1(0))

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)

def argument_test(function):
    def wrapper(x):
        print('trying wrapper before')
        function(x)
        print('trying after wrapper')
    return wrapper

def foo(x):
    print('hello',x)

test = argument_test(foo)

test('monica')
