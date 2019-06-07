from uiautomator import Device

class Core(object):
    """
    add responsibility to the core
    how to call :  self.device_mobile = self.device(self.data)
    data is from yaml file
    """
    def device(self, *args, **data_result):
        """
        Defining main device class, for consumers all management device.
        """
        try:
            return Device(*args, **data_result)

        except Exception as Argument:
            raise ValueError(Argument)
