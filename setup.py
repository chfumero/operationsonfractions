from setuptools import setup

setup(
    name='mn_eval',
    version='0.1.0',
    packages=['mn_eval'],
    entry_points={
        'console_scripts': [
            'mn_eval = mn_eval.__main__:main'
        ]
    })
