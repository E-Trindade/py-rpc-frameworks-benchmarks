import xmlrpc.client
import time
import json


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer

tests = [
    ('f1_noop', lambda p: p.f1_noop()),
    ('f2_square', lambda p: p.f2_square(0)),
    ('f3_mean_8', lambda p: p.f3_mean_8(1, 2, 3, 4, 5, 6, 7, 8)),
    ('f4_str_is_palindrome', lambda p: p.f4_str_is_palindrome('arara')),
    ('f5_exp_rep_string', lambda p: p.f5_exp_rep_string('abc')),
    ('f6_create_employee', lambda p: p.f6_create_employee(None)),
    ('f7_get_employee', lambda p: p.f7_get_employee(1)),
    ('f8_get_employee_complete', lambda p: p.f8_get_employee_complete(1))
]

def run_benchmark():
    with xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True) as proxy:
        print('test_name', 'duration_ms')
        for test_name, test in tests:
            start = time.time()
            res = test(proxy)
            end = time.time()
            print(test_name, end - start)


if __name__ == '__main__':
    run_benchmark()
