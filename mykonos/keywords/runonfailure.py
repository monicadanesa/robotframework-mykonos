from robot.libraries import BuiltIn
BUILTIN = BuiltIn.BuiltIn()
from decorator import decorator

class RunOnFailureKeywords(object):

    def __init__(self):
        self.run_on_failure_keyword = None
        self.running_on_failure_routine = False

    def register_keyword_to_run_on_failure(self, keyword):
        old_keyword = self.run_on_failure_keyword
        old_keyword_text = old_keyword if old_keyword is not None else "Nothing"

        new_keyword = keyword if keyword.strip().lower() != "nothing" else None
        new_keyword_text = new_keyword if new_keyword is not None else "Nothing"

        self.run_on_failure_keyword = new_keyword
        self._info('%s will be run on failure.' % new_keyword_text)

        return old_keyword_text

    def run_on_failure(self):
        if self.run_on_failure_keyword is None:
            return
        elif self.running_on_failure_routine:
            return
        self.running_on_failure_routine = True
        try:
            BUILTIN.run_keyword(self.run_on_failure_keyword)
        except Exception as err:
            self.run_on_failure_error(err)
        finally:
            self.running_on_failure_routine = False

    def run_on_failure_error(self, err):
        err = "Keyword '%s' couldn't be run on failure: %s" % (self.run_on_failure_keyword, err)
        if hasattr(self, '_warn'):
            self._warn(err)
            return
        raise Exception(err)
