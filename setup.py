#!/usr/bin/env python

import sys
from setuptools import setup

setup_requires = []
install_requires = ["PLY>=3.4"]

if sys.version_info < (2,7):
    setup_requires.append("unittest2")

setup(
    name='jspy',
    version='1.0',
    description='JavaScript interpreter in Python',
    author='Marek Stepniowski',
    author_email='marek@stepniowski.com',
    url='http://github.com/zuber/jspy',
    setup_requires=setup_requires,
    install_requires=install_requires,
    platforms='Cross Platform',
    packages=['jspy'],
    package_data={'jspy': ['test_files/*.js']},
    entry_points = {
        'console_scripts' : ["jspy = jspy:_main"],
    },
    zip_safe=False,
    test_suite='jspy.compat.test_collector',
    use_2to3=True,
)
