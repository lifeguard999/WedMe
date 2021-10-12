import unittest
import lib.db
import web.bindings


class TestBindings(unittest.TestCase):

    def setUp(self):
        lib.db.init()

    def _verify_products_dict(self, products):
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 1)
        self.assertIsInstance(products[0], dict)
        self.assertIn('id', products[0])
        self.assertIn('name', products[0])
        self.assertIsInstance(products[0]['name'], str)
        self.assertIn('in_stock_quantity', products[0])
        self.assertIsInstance(products[0]['in_stock_quantity'], int)
        # derived fields:
        self.assertIn('price_fmt', products[0])
        self.assertIsInstance(products[0]['price_fmt'], str)
        self.assertIn('currency', products[0])
        self.assertIsInstance(products[0]['currency'], str)

    def test_get_available_products(self):
        products = web.bindings.get_available_products()
        self._verify_products_dict(products)

    def test_workflow(self):
        # move to basket
        web.bindings.add_to_basket(1, 1)
        web.bindings.add_to_basket(2, 1)
        products = web.bindings.get_basket_products()
        self.assertEqual(2, len(products))
        self._verify_products_dict(products)
        # purchase basket
        web.bindings.purchase_basket()
        products = web.bindings.get_purchased_products()
        self.assertEqual(2, len(products))
        self._verify_products_dict(products)
