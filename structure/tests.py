from django.test import TestCase
from templatetags.structure_extras import columns


class ColumnsTestCase(TestCase):
    def test_equal_columns(self):
        data = ["a"] * 10

        new_lists, max_length = columns(data, 2)

        self.assertEqual(len(new_lists), 2)
        self.assertEqual(len(new_lists[0]), len(new_lists[1]))
        self.assertEqual(len(new_lists[0]), max_length)

    def test_one_extra_item_added_to_first_list(self):
        data = ["a"] * 11

        new_lists, max_length = columns(data, 2)

        self.assertEqual(len(new_lists), 2)
        self.assertGreater(len(new_lists[0]), len(new_lists[1]))
        self.assertEqual(len(new_lists[0]), len(new_lists[1]) + 1)
        self.assertEqual(len(new_lists[0]), max_length)

    def test_multiple_extra_item_added_evenly(self):
        data = ["a"] * 11

        new_lists, max_length = columns(data, 3)

        self.assertEqual(len(new_lists), 3)
        self.assertEqual(len(new_lists[0]), 4)
        self.assertEqual(len(new_lists[1]), 4)
        self.assertEqual(len(new_lists[2]), 3)
        self.assertEqual(max_length, 4)