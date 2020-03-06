__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"

from array_merger import *
import unittest


class TestTwoEmptyLists(unittest.TestCase):
    def test_two_empty_lists(self):
        list1 = []
        list2 = []
        expected_output = []
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)


class TestOneEmptyList(unittest.TestCase):
    def test_first_list_empty(self):
        list1 = []
        list2 = [0]
        expected_output = [0]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)

    def test_second_list_empty(self):
        list1 = [0]
        list2 = []
        expected_output = [0]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)