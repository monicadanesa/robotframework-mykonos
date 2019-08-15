import types
import multiprocessing

class DeviceUtils(object):
    def __init__(self):
        pass

    def devices_close(func):

        def wrapper(self, *argument, **settings):

            if 'devices' in settings:
                devices = settings['devices']
                del settings['devices']

                list = []
                if isinstance(devices, str):
                    return func(self, device=devices, *argument, **settings)
                else:
                    list = [func(self, device=d, *argument, **settings) for d in devices]

                    return list

            else:
                return func(self, device=None, *argument, **settings)

        return wrapper
