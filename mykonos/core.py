import attr
from uiautomator import Device

@attr.s
class Core:
    data = attr.ib()

    def __attrs_post_init__(self):
        self.data_result = self.data['setting_device']

    def device_mobile(self):
        try:
            for i in self.data_result:
                if 'device' in self.data_result and 'adb_server_host' in self.data_result and 'adb_server_port' in self.data_result:
                    device_mobile = Device(self.data_result['device'], adb_server_host=self.data_result['adb_server_host'], adb_server_port=self.data_result['adb_server_port'])
                elif 'device' in self.data_result and 'adb_server_host' in self.data_result:
                    device_mobile = Device(self.data_result['device'], adb_server_host=self.data_result['adb_server_host'])
                elif 'device' in self.data_result:
                    device_mobile = Device(self.data_result['device'])

            return device_mobile
        except Exception as Argument:
            raise ValueError(Argument)
