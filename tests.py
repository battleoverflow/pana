"""
    Project: Pana (https://github.com/azazelm3dj3d/pana)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
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
        self.assertEqual(Pana.check_user("azazelm3dj3d"), [
            ['pypi', False], # Exists
            ['npm', False], # Exists
            ['nuget', False], # Exists
            ['crates/docs', False] # Exists
        ])

if __name__ == '__main__':
    unittest.main()
