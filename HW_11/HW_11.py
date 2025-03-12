# 1.
def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not (isinstance(arg, (int, float)) and arg > 0):
                raise ValueError(f"{arg} не является положительным числом.")
        for key, value in kwargs.items():
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError(f"{key}={value} не является положительным числом.")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def my_function(a, b, c):
    return a + b + c


print(my_function(7, 8, 9))
try:
    print(my_function(-7, 8, 9))
except ValueError as e_value:
    print(e_value)


# 2.
def check_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print(f"Ошибка: {result} не является числом.")
        return result
    return wrapper


@check_numbers
def adding(a, b):
    return a + b


@check_numbers
def hello(name):
    return f"Привет, {name}!"


print(adding(8, 8))
print(hello("Bob"))


# 3.
def typed(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            converted_args = [expected_type(arg) for arg in args]
            converted_kwargs = {key: expected_type(value) for key, value in kwargs.items()}

            result = func(*converted_args, **converted_kwargs)

            return result
        return wrapper
    return decorator


@typed(expected_type=str)
def add_str(a, b):
    return a + b


print(add_str("3", 5))
print(add_str(5, 5))
print(add_str('a', 'b'))


@typed(expected_type=int)
def add_int(a, b, c):
    return a + b + c


print(add_int(5, 6, 7))


@typed(expected_type=float)
def add_float(a, b, c):
    return a + b + c


print(add_float(0.1, 0.2, 0.4))


# 4.
def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]

        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)
