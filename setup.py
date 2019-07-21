from setuptools import setup
from setuptools import setup, find_packages

version = '1.3.0'

setup(
    name='mykonos',
    version=version,
    description='Robot Framework Mobile Test Automation using UIAutomator',
    url='https://github.com/monicadanesa/mykonos',
    author='Monica Danesa and Ahmad Kadafi',
    author_email='monicadanesa@gmail.com, andriana.khadafi@gmail.com',
    keywords='Robot Framework Mobile Test Automation using UIAutomator',
    packages=find_packages(exclude=["demo", "docs", "tests", ]),
    install_requires=[
        'uiautomator >= 0.1.28', 'alog', 'robotframework >= 2.6.0'
    ],
    tests_require=[
        'pyyaml', 'pytest', 'pytest-html', 'pytest-mock', 'mock'
    ])
