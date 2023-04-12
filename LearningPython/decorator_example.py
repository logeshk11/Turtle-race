import time
import logging

def time_cal(fn):
    start = time.time()
    fn()
    print(f"Time for executing func {fn.__name__}: ", time.time() - start)
    return fn


def log(fn):
    start = time.time()
    print(f'calling func {fn.__name__} ')
    val = fn()
    with open('decorator_fn_output.txt', 'w') as f:
        f.write(f'Value returned by {fn.__name__} is {val}')
    return fn


@log
@time_cal
def sample():
    time.sleep(0.5)
    return "Sample test 2"


@log
@time_cal
def print_test():
    time.sleep(0.7)
    print("Test")
    return "test 1 printed"
