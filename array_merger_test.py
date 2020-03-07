__author__ = "Zelin Cai, Patrick Silvestre"
__version__ = "0.1.0"
__license__ = "MIT"

from array_merger import *
import unittest


class TestTwoEmptyLists(unittest.TestCase):
    def test_01_two_empty_lists(self):
        """
        Nodes:
        1-2-3-8-10-12
        """
        list1 = []
        list2 = []
        expected_output = []
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)


class TestOneEmptyList(unittest.TestCase):
    def test_02_first_list_empty(self):
        """
        Nodes:
        1-2-3-8-
            10-11-
            10-12
        """
        list1 = []
        list2 = [0]
        expected_output = [0]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)

    def test_03_second_list_empty(self):
        """
        Nodes:
        1-2-3-
            8-9-
            8-10-12
        """
        list1 = [0]
        list2 = []
        expected_output = [0]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)


class TestFullLists(unittest.TestCase):
    def test_04_list1_with_leftover_values(self):
        """
        Nodes:
        1-2-
            3-4-6-7-
            3-4-6-7-
            3-4-6-7-
            3-
                8-9-
                8-9-
                8-9-
                8-9-
                8-10-12
        """
        list1 = [3, 4, 5, 6]
        list2 = [0, 1, 2]
        expected_output = [0, 1, 2, 3, 4, 5, 6]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)

    def test_05_list2_with_leftover_values(self):
        """
        Nodes:
        1-2-
            3-4-5-7-
            3-4-5-7-
            3-4-5-7-
            3-8-
                10-11-
                10-11-
                10-11-
                10-11-
                10-12
        """
        list1 = [0, 1, 2]
        list2 = [3, 4, 5, 6]
        expected_output = array_merger(list1, list2)
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)

    def test_06_same_sized_lists(self):
        """
        Nodes:
        1-2-3-4-5-7-
            3-4-6-7-
            3-4-5-7-
            3-4-6-7-
            3-4-5-7-
            3-4-6-7-8-10-12
        """
        list1 = [0, 2, 4]
        list2 = [1, 3, 5]
        expected_output = [0, 1, 2, 3, 4, 5]
        actual_output = array_merger(list1, list2)
        self.assertEqual(expected_output, actual_output)
