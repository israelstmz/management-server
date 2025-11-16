import sys


pipe = sys.stdout

def logs_pipe(new_pipe):
    global pipe
    pipe = new_pipe

def log(log_string: str):
    print(log_string, file=pipe, end="", flush=True)
