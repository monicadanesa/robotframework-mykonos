import types
import multiprocessing
from mykonos.keywords.management_device import ManagementDevice


class Setup():

    def __init__(self):
        pass

    def __clean_dot_on_version(self, version_android=None):
        if '.' in version_android:
            version_android = version_android.split('.')
            return int(version_android.pop(0))
        else:
            return int(version_android)

    def __device_check(self, **settings):

        if 'device' in settings:
            get_device = settings['device']

            if isinstance(get_device, str):
                return next(ManagementDevice().get_android_version(device=get_device))
            else:
                versions = ManagementDevice().get_android_version(device=get_device)
                version_list = []
                for version in versions:
                    version_list.append(version)

                return version_list
        else:
            return next(ManagementDevice().get_android_version())

    def remove_dot_version(self, **settings):
        version_android = self.__device_check(**settings)
        list_version = []
        if isinstance(version_android, str):
            return self.__clean_dot_on_version(version_android)
        else:
            for version in version_android:
                list_version.append(self.__clean_dot_on_version(version))

            return list_version


class Decorators(object):

    def __init__(self):
        pass

    def android_version(func):

        def wrapper(self, *argument, **settings):
            management_device = ManagementDevice()
            setup = Setup()
            get_version_android = management_device.get_android_version()

            if len(list(get_version_android)) == 1 or 'device' in settings:

                version = setup.remove_dot_version(**settings)

                if 'text' in settings:
                    text = settings['text']
                    del settings['text']

                    if int(version) >= 9:
                        text_name = text.upper()
                        func(self, text=text_name, *argument, **settings)
                    else:
                        func(self, text=text, *argument, **settings)
                else:
                    func(self, *argument, **settings)


        return wrapper

class Parallel(object):

    def __init__(self):
        pass

    def device_check(func):

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
