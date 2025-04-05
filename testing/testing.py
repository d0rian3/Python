# tests.py
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()


"""
Методы setUp и tearDown
Если добавить методы setUp и tearDown, 
то код из них будет исполняться перед каждым 
тестом и после каждого теста соответственно.

Тесты в python переехали из Java. 
И это причина почему названия этих методов не соответствуют PEP8. 
Просто смирились, запомнили и пользуемся.
"""

import unittest

class TestSum(unittest.TestCase):

    def setUp(self):
        self.my_num = 5

    def test_odd(self):
        self.assertTrue(self.my_num % 2, "Number is odd")

    def tearDown(self):
        self.my_num += 1


import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()



