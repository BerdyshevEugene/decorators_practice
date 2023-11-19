import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(
            f'Время выполнения функции {func.__name__}: {execution_time} секунд')
        return result
    return wrapper


@timer
def some_function():
    time.sleep(2)
    print('Функция выполнена')


some_function()
