from setuptools import setup

setup(
    name='download-organizer',
    version='0.1',
    py_modules=['organizer'],
    install_requires=[
        'watchdog',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        dlorg=organizer:main
    ''',
)
