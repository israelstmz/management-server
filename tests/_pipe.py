class Pipe:
    def __init__(self):
        self.buffer = []

    def write(self, text):
        if text:  # prevents writing "" at the end of print
            self.buffer.append(text)

    def flush(self):
        pass  # necessary

    def __getitem__(self, item):
        return self.buffer[item]
