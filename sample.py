from yaml import load
from mykonos.orcestrator import Orcestrator


with open('test/setting.yaml') as f:
    data = load(f)

data
data

orc = Orcestrator(data)
result = orc.device_info()
result

orc.turn_on_screen()
