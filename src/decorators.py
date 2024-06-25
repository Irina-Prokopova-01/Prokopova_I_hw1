from typing import Any, Callable
from functools import wraps


def log(filename: Any) -> Callable:
    """Декоратор который логирует вызов функции и ее результат в файл или в консоль"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                # filename.write("my_function ok")
                print("my_function ok")
            except Exception as e:
                # filename.write(f"my_function error: {e}. Inputs:{args}, {kwargs}")
                print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
            return result
        return wrapper
    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))