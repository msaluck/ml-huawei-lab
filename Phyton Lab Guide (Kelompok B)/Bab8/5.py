# Construct a decorator
import time
def func(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time() 
        print('Consumed time:%s second' % (end_time - start_time))
    return inner















