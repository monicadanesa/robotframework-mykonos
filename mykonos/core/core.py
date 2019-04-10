import attr

from yaml import load
from abc import ABC, abstractmethod
from uiautomator import Device


class Decorator(ABC):

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def device(self):
        print('decorator')


class Core(Decorator):
    with open('test/setting.yaml') as f:
        data = load(f)

    data_result = data['setting_device']
    def device(self):
        try:
            for i in self.data_result:
                if 'device' in self.data_result and 'adb_server_host' in self.data_result and 'adb_server_port' in self.data_result:
                    return Device(self.data_result['device'], adb_server_host=self.data_result['adb_server_host'], adb_server_port=self.data_result['adb_server_port'])
                elif 'device' in self.data_result and 'adb_server_host' in self.data_result:
                    return Device(self.data_result['device'], adb_server_host=self.data_result['adb_server_host'])
                elif 'device' in self.data_result:
                    return Device(self.data_result['device'])

        except Exception as Argument:
            raise ValueError(Argument)
