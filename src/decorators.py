from typing import Any, Callable
from functools import wraps

#
# def log(filename: Any) -> Callable:
#     """Декоратор который логирует вызов функции и ее результат в файл или в консоль"""
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args: Any, **kwargs: Any) -> Any:
#             try:
#                 result = func(*args, **kwargs)
#                 # filename.write("my_function ok")
#                 print("my_function ok")
#             except Exception as e:
#                 # filename.write(f"my_function error: {e}. Inputs:{args}, {kwargs}")
#                 print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
#             return result
#         return wrapper
#     return decorator
#
# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x + y
#
# print(my_function(1, 2))

#
# def log(filename: str | None = None) -> Callable:
#     """Декоратор который логирует вызов функции и ее результат в файл или в консоль"""
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args: Any, **kwargs: Any) -> Any:
#
#             try:
#                 result = func(*args, **kwargs)
#                 # filename.write("my_function ok")
#                 print("my_function ok")
#             except Exception as e:
#                 # filename.write(f"my_function error: {e}. Inputs:{args}, {kwargs}")
#                 print(f"my_function error: {e}. Inputs:{args}, {kwargs}")
#             return result
#         return wrapper
#     return decorator

def log(filename: str | None = None) -> Callable:
  def decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
      try:
          result = func(*args, **kwargs)
          log_message = "my_function ok"
        # выполняешь действие и записывай в log_message сообщение, которуешь будешь записывать в файл
      except Exception as e:
          log_message = f"my_function error: {e}. Inputs:{args}, {kwargs}"
        # выполняешь действие если ошибка и записывай в log_message сообщение, которуешь будешь распечатать
      if filename:
        with open(filename, "a", encoding="utf-8") as file:
          file.write(log_message)
      else:
        print(log_message)
      return result
    return wrapper
  return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))