# -*- coding: utf-8 -*-

import unittest
from .context import foo

"""
test_foo
"""
class FooTests(unittest.TestCase):
    """
    FooTests
    """
    def test_bar(self):
        """Test bar."""
        assert foo.bar() is True

if __name__ == '__main__':
    unittest.main()