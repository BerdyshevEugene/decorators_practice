import time


def logger(func):
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log.txt', 'a') as file:
            file.write(
                f'{timestamp} - Вызов функции {func.__name__} с аргументами {args} {kwargs}\n')
        result = func(*args, **kwargs)
        return result
    return wrapper


@logger
def some_function(arg_1, arg_2):
    print('Функция выполнена!')
    return arg_1 + arg_2


some_function(2, 3)
