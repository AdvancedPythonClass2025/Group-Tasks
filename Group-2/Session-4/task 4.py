class Logger:
    def __init__(self, filename="log.txt"):
        self.filename = filename

def log_activity(self, func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(self.filename, "a", encoding= "utf-8") as file:
