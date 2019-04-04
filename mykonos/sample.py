from yaml import load
from mykonos.orcestrator import Orcestrator


with open('setting.yaml') as f:
    data = load(f)

data
data



print(device_mobile)

device_mobile
orc = Orcestrator(data)
result = orc.device_info()
result
