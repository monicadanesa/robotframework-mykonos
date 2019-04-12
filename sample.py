from yaml import load
from mykonos.keywords.key_event import KeyEvent
from mykonos.keywords.management_device import ManagementDevice


with open('test/setting.yaml') as f:
    data = load(f)

data

data_result = data['setting_device']

key_event = KeyEvent(data)

key_event
key_event.press_navigation('menu()')

key_event.press_menu()

key_event.device_info()
orc.turn_on_screen()
