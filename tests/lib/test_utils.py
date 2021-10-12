import unittest
import lib.utils as utils


class TestUtils(unittest.TestCase):

    def test_memoize_noargs(self):
        counter = [0]
        @utils.memoize
        def test_func():
            counter[0] += 1
            return 1
        self.assertEqual(1, test_func())
        self.assertEqual(1, test_func())
        self.assertEqual(1, counter[0])

    def test_memoize_args(self):
        counter = [0]
        @utils.memoize
        def test_func(x):
            counter[0] += 1
            return x
        self.assertEqual(1, test_func(1))
        self.assertEqual(1, test_func(1))
        self.assertEqual(2, test_func(2))
        self.assertEqual(2, test_func(2))
        self.assertEqual(2, counter[0])

    def test_get_project_path(self):
        path = utils.get_project_path()
        self.assertIsInstance(path, str)
        self.assertGreater(len(path), 5)

    def test_fmt_price(self):
        self.assertEqual('123.40', utils.fmt_price(123.4))
        self.assertEqual('1,123.40', utils.fmt_price(1123.4))
        self.assertEqual('1,123.24', utils.fmt_price(1123.24323))