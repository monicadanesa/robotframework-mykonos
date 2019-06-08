from setuptools import setup
from setuptools import setup, find_packages


setup(
    name='mykonos',
    version='0.0.1',
    description='Robot Framework Mobile Test Automation using UIAutomator',
    url='https://github.com/monicadanesa/mykonos',
    author='Monica Danesa and Ahmad Kadafi',
    author_email='monicadanesa@gmail.com, andriana.khadafi@gmail.com',
    keywords='Robot Framework Mobile Test Automation using UIAutomator',
    packages=find_packages(exclude=["demo", "docs", "tests", ]),
    install_requires=[
        'robotframework', 'uiautomator', 'alog', 'selenium', 'imgutil'
    ],
    test_requires=[
        'pyyaml', 'pytest', 'pytest-html', 'pytest-mock', 'mock'
    ])
