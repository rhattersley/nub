from contextlib import contextmanager
from time import time


@contextmanager
def timeit(label):
    t0 = time()
    yield
    print '{}: {} s'.format(label, time() - t0)
