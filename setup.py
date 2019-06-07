from setuptools import setup

setup(
    name='mykonos',
    version='0.0.1',
    description='Robot Framework Mobile Test Automation using UIAutomator',
    packages=['mykonos'],
    install_requires=[
        'uiautomator', 'robotframework'
    ],
    entry_points={'console_scripts': ['mykonos = mykonos.__init__:mykonos']})
