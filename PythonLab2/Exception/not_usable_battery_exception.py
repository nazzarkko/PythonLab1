class NotUsableBattery(Exception):
    message = "Battery is not usable!"

    def __init__(self):
        super().__init__(self.message)
