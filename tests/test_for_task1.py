import sys
sys.path.insert(0, '../')
from task1 import *
from unittest import TestCase

my_object = Counter()

class CounterTestCase(TestCase):
    def setUp(self):
        self.count_test_data = [
            [[1,1,1,1,1,1], 4000], [[1,1,1,2,3,5], 1050], [[1,2,3,4,5,6], 1500], [[6,6,5,4,5,6], 700],
            [[1,2,5,3,2,1], 250], [[2,2,4,4,6,6], 750], [[2,2,1,4,3,6], 100], [[1,5,1,4,3,6], 250],
            [[1,5,1,4,3,5], 300], [[1,1,1,4,3,6], 1000], [[1,5,1,6,6,6], 850]
        ]

    def test_count_test_data(self):
        for combination, expected_number in self.count_test_data:
            actual_number = my_object.count(combination)
            self.assertEqual(expected_number, actual_number)