from uiautomator import Device

class Core(object):
    """ add responsibility to the core
    how to call :  self.device_mobile = self.device(self.data)
    data is from yaml file
    """
    def device(self, data, **locator):
        data_result = data['setting_device']
        try:
            for i in data_result:
                if ('device' in data_result and
                    'adb_server_host' in data_result and
                    'adb_server_port' in data_result):
                    return Device(data_result['device'], adb_server_host=data_result['adb_server_host'], adb_server_port=data_result['adb_server_port'])

                elif ('device' in data_result and
                    'adb_server_host' in data_result):
                    return Device(data_result['device'], adb_server_host=data_result['adb_server_host'])

                elif 'device' in data_result:
                    return Device(data_result['device'])

        except Exception as Argument:
            raise ValueError(Argument)
