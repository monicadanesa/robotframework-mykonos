from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.0.2'

setup(
    name='mykonos',
    version=version,
    description='Robot Framework Mobile Test Automation using UIAutomator',
    url='https://github.com/monicadanesa/mykonos',
    license='MIT',
    author='Monica Danesa and Ahmad Kadafi',
    author_email='monicadanesa@gmail.com, andriana.khadafi@gmail.com',
    keywords=[
        'testing', 'android', 'uiautomator',
        'robotframework', 'android test'
    ],
    packages=['mykonos'],
    include_package_data=True,
    install_requires=[
         'uiautomator', 'robotframework >= 2.6.0'
    ],
    test_requires=[
        'pyyaml', 'pytest', 'pytest-html', 'pytest-mock', 'mock'
    ],
    entry_points={'console_scripts': ['mykonos = mykonos.__init__:mykonos']})
