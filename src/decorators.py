from time import time
from typing import Any


def log(filename: Any) -> Any:
    def decorators(func: Any) -> Any:
        def wrapper(*args: tuple, **kwargs: dict[str, Any]) -> Any:
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                log_result = f"{func.__name__} ok.Time in work: {end_time - start_time:.6f}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file_name:
                        file_name.write(log_result)
                print(log_result)
                return result
            except Exception as e:
                log_result = f"{func.__name__} error: {e} Inputs:{args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file_name:
                        file_name.write(log_result)
                    print(log_result)
            raise Exception("Ошибка ввода данных")

        return wrapper

    return decorators


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
