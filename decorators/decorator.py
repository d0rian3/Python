import time


def timer_decorator(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result

    return wrapper


def repeat_decorator(n):
    def decorator(func):
        def wrapper(*args):
            result = None
            for i in range(n):
                result = func(*args)
                print('Функция была вызвана')
            return result

        return wrapper

    return decorator


class FileReader:
    def __init__(self, namefile):
        self.namefile = namefile


def read_lines(self):
    with open(self.namefile, "r") as file:
        return file.readlines()


@timer_decorator
@repeat_decorator(5)
def reader():
    with open("decorator_text_file.txt", "r") as file:
        return file.readlines()




reader()
"""
Создайте класс, который будет считывать файл
Напишите декоратор, который будет замерять время выполнения.
Напишите декоратор, который будет вызывать функцию n-раз.
Воспользуйтесь декоратором для замера времени 
и примените его ко всем функциям в вашем модуле.
"""

from collections import defaultdict

functions_counter = defaultdict(int)


def counter(function):
    def wrapper(*args, **kwargs):
        functions_counter[function.__name__] += 1
        print(f"{functions_counter[function.__name__]} - times was working {function.__name__}")
        return function(*args, **kwargs)

    return wrapper


def errors_checker(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(f"error {e}")
            return False

    return wrapper


limit_function_counter = defaultdict(int)


def counter_limit(n):
    def limit_counter(function):
        def wrapper(*args, **kwargs):

            limit_function_counter[function.__name__] += 1
            if limit_function_counter[function.__name__] > n:
                print("Запрет")
            else:
                print("Okey")

        return wrapper
    return limit_counter


@counter
def test1():
    print("äsd")


@counter
def test2():
    print("jpeg")


test2()
test1()
test1()


@errors_checker
def calculate(a: int) -> int:
    return a / 0


result = calculate(10)
print(result)

@counter_limit(2)
def show():
    print("Tested func")

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Вызывается say_hello...")
        return func(*args, **kwargs)
    return wrapper


@log_call
def say_hello():
    print("Привет, мир!")

say_hello()



