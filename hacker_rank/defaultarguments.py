from testcases import PRINT_ORDER

class EvenStream(object):
    def __init__(self):
        self.current = 0
        print('init even')

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1
        print('init odd')

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())

for order in PRINT_ORDER:
    stream_name, n = order.split()    
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())