def wrapper(func):
    def inner():
        print('before')
        func()
        print('after')

    return inner


@wrapper
def say_something():
    print('something')


say_something()
