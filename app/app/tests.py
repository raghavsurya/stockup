from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    def test_add_two_nums(self):
        res = calc.add(5, 7)
        self.assertEqual(res, 12)
