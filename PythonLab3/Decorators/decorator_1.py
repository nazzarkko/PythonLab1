def to_tuple_decorator(func):
    """
    Decorator that converts the output of a function into a tuple.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, set)):
            return tuple(result)
        return result
    return wrapper
