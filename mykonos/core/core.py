from uiautomator import Device

class Core(object):
    """
    add responsibility to the core
    how to call :  self.device_mobile = self.device(self.data)
    data is from yaml file
    """
    def device(self, *args, **setting):
        """
        Defining main device class, for consumers all management device.
        """
        try:
            return Device(*args, **setting)

        except Exception as Argument:
            raise ValueError(Argument)
