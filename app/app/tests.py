"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test Calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subs_numbers(self):
        """Test subtracting numbers together"""

        res = calc.subs(7,5)

        self.assertEqual(res, 2)