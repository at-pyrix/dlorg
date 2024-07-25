from setuptools import setup, find_packages

setup(
    name='download-organizer',
    version='1.4',
    description='A Python script to organize your downloads folder by file extensions and watch for new files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pyrix',
    url='https://github.com/at-pyrix/download-organizer',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'colorama',
    ],
entry_points={
    'console_scripts': [
        'dlorg=organizer.organizer:main',
    ],
},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
)
