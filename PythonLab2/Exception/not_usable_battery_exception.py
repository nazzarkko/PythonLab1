"""
This module defines the custom exception class NotUsableBattery.
"""


class NotUsableBattery(Exception):
    """
    Custom exception class for representing a not-usable battery.
    """

    message = "Battery is not usable!"

    def __init__(self):
        """
        Initializes a new instance of the NotUsableBattery class.
        """
        super().__init__(self.message)
