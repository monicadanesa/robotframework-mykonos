from robot.libraries.BuiltIn import BuiltIn
from mykonos.core.core import Core

class PreRequest(Core):
    def __init__(self):
        self.built_in = BuiltIn()

    def set_test_rail_id(self, testid=None):
        """The keyword for set test rail id

        ***Example:***
        || Set Test Id | id_of_test
        || Example : Set Test Rail Id | 568787
        """
        if testid is not None:
            test = self.built_in.set_test_variable("${TEST_ID}", "%s" % (testid))
        else:
            raise ValueError("Test id didn't set with id: %s" % (testid))
