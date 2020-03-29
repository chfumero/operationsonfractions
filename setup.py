from setuptools import setup

setup(
    name='operationsonfractions',
    version='0.1.0',
    packages=['operationsonfractions'],
    entry_points={
        'console_scripts': [
            'operationsonfractions = operationsonfractions.__main__:main'
        ]
    })
