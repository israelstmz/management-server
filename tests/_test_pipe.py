class Pipe:
    """
    Designed to receive logs during testing for control purposes.
    """
    def __init__(self):
        self.buffer = []

    def send(self, text):
        """
        Duty, log collection point.
        :param text:
        :return:
        """
        self.buffer.append(text)

    def __getitem__(self, item):
        return self.buffer[item]
