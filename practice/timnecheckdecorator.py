import functools
from time import time
import threading

# Thread-local variable so depth is safe even if multiple functions run
_depth = threading.local()
_depth.value = 0  

def track_depth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _depth.value += 1
        depth = _depth.value
        # print(f"{'  ' * (depth-1)}Entering {func.__name__}, depth={depth}")
        
        # inject depth into kwargs (function can accept it if it wants)
        result = func(*args, depth=depth, **kwargs)
        
        # print(f"{'  ' * (depth-1)}Leaving {func.__name__}, depth={depth}")
        _depth.value -= 1
        return result
    return wrapper




def timecheck(func):
    @functools.wraps(func)
    @track_depth
    def wrapper(*args, depth=None,  **kwargs):
        start_time  = time()
        result = func(*args, **kwargs)
        elapsed_time = time()-start_time
        if depth < 2:
            print(f'elapsed time in seconds {elapsed_time} at stack depth of {depth}')
        else:
            print(f'stack depth {depth}')
        return result 
    return wrapper



@timecheck
def fibonacci(n):
    """Compute nth Fibonacci number recursively (slow)."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))
