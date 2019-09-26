from robot.libraries.BuiltIn import BuiltIn
from mykonos.core.core import Core
from mykonos.keywords.element import GlobalElement

class PreRequest(Core):
    def __init__(self):
        self.built_in = BuiltIn()
        self.global_el = GlobalElement()

    def set_test_rail_id(self, test_id=None):
        """The keyword for set test rail id

        ***Example:***
        || Set Test Rail Id | id_of_test
        || Example : Set Test Rail Id | 568787
        """
        if test_id is not None:
            self.built_in.set_test_variable("${TEST_ID}", "%s" % (test_id))
        else:
            raise ValueError("Test id didn't set with id: %s" % (test_id))

    def capture_screen_when_failed_test(self):
        """The keyword for capturing the device screen when failed test

        ***Example:***
        || Capture Screen When Failed Test
        """
        test_status = self.built_in.get_varibale_value("${TEST_STATUS}")
        print(test_status)
        if test_status is True:
            self.global_el.capture_screen("devices_parallel='${emulator})'")
        else:
            raise ValueError("Test can't be captured")
