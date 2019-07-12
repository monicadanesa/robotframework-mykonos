from mykonos.keywords.management_device import ManagementDevice
import types

class Decorators(object):

    def __init__(self):
        pass

    def android_version(func):

        def wrapper(self, *argument, **settings):

            if 'version' in settings:
                version = settings['version']
                del settings['version']
            else:
                get_version_android = ManagementDevice().get_android_version()

                if len(list(get_version_android)) == 1:

                    version_android = next(ManagementDevice().get_android_version())

                    print(version_android)
                    if '.' in version_android:
                        version_android = version_android.split('.')
                        version = int(version_android.pop(0))
                    else:
                        print(version_android)
                        version = int(version_android)

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
                else:
                    print('device is more than 1')

        return wrapper
