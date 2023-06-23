import time


def measure_execution_time(func):
    """
    Decorator that measures the execution time of a method and prints it to the console.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result

    return wrapper
