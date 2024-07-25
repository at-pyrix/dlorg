from setuptools import setup, find_packages

setup(
    name='download-organizer',
    version='0.1',
    description='A Python script to organize your downloads folder by file extensions and watch for new files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/download-organizer',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dlorg=organizer:main',
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
