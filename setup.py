from setuptools import setup

setup(
    name='dlorg',
    version='2.2',
    description='A Python script to organize your downloads folder by file extensions and mimetypes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pyrix',
    url='https://github.com/at-pyrix/dlorg',
    py_modules=['dlorg'],
    install_requires=[
        'colorama>=0.4.4',
        'python-magic>=0.4.27'
    ],
    entry_points={
        'console_scripts': [
            'dlorg=dlorg:main',
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
