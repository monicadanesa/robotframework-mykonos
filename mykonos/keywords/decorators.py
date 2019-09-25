import types
import multiprocessing
from functools import wraps

class Parallel(object):

    def __init__(self):
        pass

    def device_check(func):
        @wraps(func)
        def wrapper(self, *argument, **settings):

            if 'devices_parallel' in settings:
                devices_parallel = settings['devices_parallel']
                del settings['devices_parallel']

                list = []
                if isinstance(devices_parallel, str):
                    return func(self, device=devices_parallel, *argument, **settings)
                else:
                    list = [func(self, device=d, *argument, **settings) for d in devices_parallel]
                    return list
            else:
                return func(self, device=None, *argument, **settings)

        return wrapper
