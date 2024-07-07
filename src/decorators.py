import sys
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор логирует вызов функции и
    ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok"
            except Exception as e:
                log_message = f"my_function error: {e}. Inputs:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
                    print(log_message, file=sys.stderr)
            else:
                print(log_message, file=sys.stderr)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function("1", 2))

# from config import ROOT_PATH
# from pathlib import Path

#
# def log(filename=None):
#     """Декоратор логирует вызов функции и
#     ее результат в файл или в консоль"""
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args: Any, **kwargs: Any) -> Any:
#             try:
#                 result = func(*args, **kwargs)
#                 if filemane:
#                     with open(Path(ROOT_PATH, filename), 'a') as mylog:
#                         mylog.write(f'{func.__name__} ok\n')
#                 else:
#                     print(f'{func.__name__} ok\n')
#                 return result
#             except Exception as e:
#                 if filename:
#                     with open(Path(ROOT_PATH, filename), 'a') as mylog:
#                         mylog.write(f'{func.__name__} error: {e}. Inputs: {args} {kwargs}\n')
#                 else:
#                     print(f'{func.__name__} error: {e}. Inputs: {args} {kwargs}\n')
#                 raise e
#             return wrapper
#         return decorator
