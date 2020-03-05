__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"

from array_merger import *
import unittest

class test(unittest.TestCase):
    def test1(self):
        list1 = [1, 2, 7, 11]
        list2 = [3, 7, 13, 16, 29]
        merged_list = array_merger(list1, list2)
        expected_list = [1, 2, 3, 7, 7, 11, 13, 16, 29]
        self.assertEqual(merged_list, expected_list)
