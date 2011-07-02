#!/usr/bin/env python

import sys
from setuptools import setup

setup_requires = []
install_requires = []

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
    packages=['jspy', 'ply'],
    scripts=['scripts/jspy'],
    test_suite='jspy.compat.test_collector',
)
