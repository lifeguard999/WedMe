import unittest
import lib.db


class TestDb(unittest.TestCase):

    def test_get_products_dict(self):
        d = lib.db._load_products_list()
        self.assertIsInstance(d, list)
        self.assertGreater(len(d), 7)
        self.assertIsInstance(d[0], dict)
        self.assertIn('id', d[0])
        self.assertIn('name', d[0])
        self.assertIsInstance(d[0]['name'], str)
        self.assertIn('in_stock_quantity', d[0])
        self.assertIsInstance(d[0]['in_stock_quantity'], int)
        # derived fields:
        self.assertIn('price', d[0])
        self.assertIsInstance(d[0]['price'], float)
        self.assertIn('currency', d[0])
        self.assertIsInstance(d[0]['currency'], str)

    def test_move(self):
        self.assertEqual(0, len(lib.db.AVAILABLE))
        self.assertEqual(0, len(lib.db.PRODUCT_DATA))
        lib.db.init()
        self.assertGreater(len(lib.db.AVAILABLE), 7)
        self.assertGreater(len(lib.db.PRODUCT_DATA), 7)
        self.assertEqual(0, len(lib.db.BASKET))
        lib.db.move(lib.db.AVAILABLE, lib.db.BASKET, 1, 1)
        lib.db.move(lib.db.AVAILABLE, lib.db.BASKET, 2, 1)
        self.assertEqual(2, len(lib.db.BASKET))
        self.assertEqual(0, len(lib.db.PURCHASED))
