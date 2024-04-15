"""
    Project: Pana (https://github.com/battleoverflow/pana)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

import unittest
from pana import Pana

class TestPana(unittest.TestCase):
    def test_pkg_exists(self):
        self.assertEqual(Pana.check_pkg("pana"), [
            ['pypi', False], # Exists
            ['npm', False], # Exists
            ['nuget', True], # Does not exist
            ['crates/docs', False] # Exists
        ])

    def test_user_exists(self):
        self.assertEqual(Pana.check_user("battleoverflow"), [
            ['pypi', False], # Exists
            ['npm', False], # Exists
            ['nuget', False], # Exists
            ['crates/docs', False] # Exists
        ])

if __name__ == '__main__':
    unittest.main()
