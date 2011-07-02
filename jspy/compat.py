# Compatibility layer over some python stdlib modules


__all__ = (
    'unittest',
    'test_collector'
)

import sys
import os

try:
    import unittest2 as unittest
except ImportError:
    if sys.version_info >= (2, 7):
        import unittest
    else:
       raise Exception("You need to have unittest2 or Python >= 2.7 installed.")


try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO # PyPy doesn't need the C implementation

def test_collector():
    # import __main__ triggers code re-execution
    __main__ = sys.modules['__main__']
    setupDir = os.path.abspath(os.path.dirname(__main__.__file__))
    return unittest.loader.defaultTestLoader.discover(setupDir)
