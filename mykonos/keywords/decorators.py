from mykonos.keywords.management_device import ManagementDevice
import types


class Setup():
    def __init__(self):
        pass

    def remove_dot_version(self, **settings):
        version_android = self.__device_check(**settings)

        if '.' in version_android:
            version_android = version_android.split('.')
            return int(version_android.pop(0))
        else:
            return int(version_android)

    def __device_check(self, **settings):

        if 'device' in settings:
            get_device = settings['device']

            return next(ManagementDevice().get_android_version(device=get_device))
        else:
            return next(ManagementDevice().get_android_version())


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
