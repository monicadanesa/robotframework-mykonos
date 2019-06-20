import traceback
from alog import debug, info, error
from mykonos.core.core import Core


class LocatorElement(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def get_locator(self, *argument, **settings):
        """Access locator from device.

        **selector support:**

        * text, textContains, textMatches, textStartsWith
        * className, classNameMatches
        * description,descriptionContains,descriptionMatches,descriptionStartsWith
        * checkable, checked, clickable, longClickable
        * scrollable, enabled,focusable, focused, selected
        * packageName, packageNameMatches
        * resourceId, resourceIdMatches
        * index, instance


        **Example:**

        || ${locator}= Get Locator           | text=sample text

        """
        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings)
        else:
            return self.device_mobile(*argument, **settings)

    def get_child(self, parent, *argument, **settings):
        """Access child locator from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${child}=   Get Child           | parent=${locator}  text=sample text
        """
        return parent.child(*argument, **settings)

    def get_sibling(self, parent, *argument, **settings):
        """Access sibling locator from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${sibling}=   Get Sibiling      | parent=${locator}  text=sample text
        """
        return parent.sibling(*argument, **settings)

    def left_position(self, parent, *argument, **settings):
        """Access left position from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${left}=     Left Position      | parent=${locator}  text=sample text
        """
        return parent.left(*argument, **settings)

    def right_position(self, parent, *argument, **settings):
        """Access left position from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${right}=    Right Position     | parent=${locator}  text=sample text
        """
        return parent.right(*argument, **settings)

    def up_position(self, parent, *argument, **settings):
        """Access left position from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${up}=    Up Position           | parent=${locator}  text=sample text
        """
        return parent.up(*argument, **settings)

    def down_position(self, parent, *argument, **settings):
        """Access left position from device.

        **Example:**

        || ${locator}=  Get Locator        | text=sample text

        || ${down}=    Down Position       | parent=${locator}  text=sample text
        """
        return parent.down(*argument, **settings)

    def get_locator_by_index(self, *argument, **settings):
        """Get Element locator by index on device.

        **Example:**

        || Get Locator By Index           | text=sample_text   | index=1

        || ${locator}=  Get Locator        | text=sample text

        || Get Locator By Index            | locator=${locator} | index=1
        """
        index = int(settings['index'])
        del settings['index']

        if 'locator' in settings:
            locator = settings['locator']
            del settings['locator']

            return locator[index]
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings)[index]
            else:
                return self.device_mobile(*argument, **settings)[index]

    def handlers(self, action, function):
        """Call customized function on device.

        **Example:**

        || Handlers                  | action=on   | function=sample_function
        """
        if 'on' in action:
            return self.device_mobile.handlers.on(function)
        elif 'off' in action:
            return self.device_mobile.handlers.off(function)


class WatcherElement(Core):
    """Class is used to perform some actions when selector cannot be found."""

    def __init__(self):
        self.device_mobile = self.device()

    def __watcher_register(self, **settings):
        name = settings['name']
        del settings['name']
        return self.device_mobile.watcher(name)

    def watcher(self, **settings):
        """Watcher is registered when a selector cannot be find.

        name=name of watcher

        WHEN, className=sample_class

        WHEN, packageName=sample_package

        **Example:**

        || ${sample_watcher}=name=sample_watcher  | className=sample_class

        || Click Element   | watcher=${sample_watcher}      | text=sample_text
        """
        name_watcher = settings['name']
        del settings['name']
        self.__watcher = self.__watcher_register(name=name_watcher)
        return self.__watcher.when(**settings)

    def watcher_action(self, action, **settings):
        """Watcher Action is used to running the action on the watcher.

        run=Force to run all watchers

        remove=Remvoe watchers

        reset=Reset all triggered watchers

        list=List all watchers

        triggered=Check if there is any watcher triggered


        **Example:**

        || Watcher Action  | action=run

        || Watcher Action  | action=remove

        || Watcher Action  | action=remove | name=sample_watcher

        || Watcher Action  | action=reset

        || Watcher Action  | action=list

        || Watcher Action  | action=triggered
        """
        if 'run' in action:
            return self.device_mobile.watchers.run()
        elif 'remove' in action:
            if 'name' in settings:
                name = settings['name']
                del settings['name']
                return self.device_mobile.watchers.remove(name)
            else:
                return self.device_mobile.watchers.remove()
        elif 'list' in action:
            return self.device_mobile.watchers
        elif 'reset' in action:
            return self.device_mobile.watchers.reset()
        elif 'triggered' in action:
            return self.device_mobile.watchers.triggered
