"""
This module defines a decorator for logging exceptions.
"""

import logging


def logged_decorator(my_exception, file_mode):
    """
    Decorator function for logging exceptions.

    Args:
        my_exception (Exception): The exception class to catch.
        file_mode (str): The mode for logging, either "console" or "file".

    Returns:
        function: The decorated function.

    """

    def decorator(func):
        """
        Decorator function that wraps the original function.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the original function.

        """
        # pylint: disable=inconsistent-return-statements
        def wrapper(*args, **kwargs):
            """
            Wrapper function that handles exceptions and logs them.

            Returns:
                The result of the original function.

            """
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
