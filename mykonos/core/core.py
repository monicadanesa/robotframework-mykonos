from abc import ABC, abstractmethod
from uiautomator import Device


class Decorator(ABC):

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def device(self):
        print('decorator')


class Core(Decorator):
    """ add responsibility to the component
    how to call : sample_a = Core(Decorator)
    sample_a.device(data_result)
    """
    def device(self, data):
        data_result = data['setting_device']
        try:
            for i in data_result:
                if 'device' in data_result and 'adb_server_host' in data_result and 'adb_server_port' in data_result:
                    return Device(data_result['device'], adb_server_host=data_result['adb_server_host'], adb_server_port=data_result['adb_server_port'])
                elif 'device' in data_result and 'adb_server_host' in data_result:
                    return Device(data_result['device'], adb_server_host=data_result['adb_server_host'])
                elif 'device' in data_result:
                    return Device(data_result['device'])

        except Exception as Argument:
            raise ValueError(Argument)
