import logging


def logged_decorator(my_exception, file_mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except my_exception as error:
                if file_mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(error)
                elif file_mode == "file":
                    logging.basicConfig(filename='result.txt', level=logging.ERROR)
                    logging.error(error)

        return wrapper

    return decorator
