from setuptools import setup
from distutils.core import setup
from console_utility_test.version import __version__
from console_utility_test.console_utility_test import __doc__

setup(
    name='python-console-utility-test',
    version=__version__,
    python_requires='>=3.4',
    description=__doc__,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='cheretbe',
    author_email='cheretbe@gmail.com',
    url='https://github.com/cheretbe/python-console-utility-test',
    license='MIT License',
    packages=['console_utility_test'],
    install_requires=['humanfriendly'],
    entry_points={
        "console_scripts": ['console_utility_test = console_utility_test.console_utility_test:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: Name Service (DNS)'
    ],
)