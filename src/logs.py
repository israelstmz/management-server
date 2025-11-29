import logging


class __Pipe(logging.Handler):
    """
    Gets a class and prepares it for a formal log pipeline.
    """
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe

    def emit(self, record):
        """
        The log from the library is sent here.
        :param record:
        :return:
        """
        self.pipe.send(
            self.format(record)  # still allows for the built-in control of the format
        )


def setup_logs_pipe(pipe, init=False):
    root = logging.getLogger()  # the logger
    if init:  # if the user wants to reset all log pipes:
        root.handlers.clear()
    root.addHandler(__Pipe(pipe))  # adding the new pipe
