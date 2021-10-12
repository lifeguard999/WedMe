import unittest
import lib.db
import web.views


def dummy_func():
    pass


class TestViews(unittest.TestCase):

    def setUp(self):
        lib.db.init()

    def _verify_page(self, page):
        self.assertIsInstance(page, str)
        self.assertGreater(len(page), 100)  # it's got the 'stuff'
        self.assertIn('Name', page)  # table's there
        self.assertIn('Gifts', page)  # menu's there

    def test_gifts_view(self):
        page = web.views.gifts_view(dummy_func)()
        self._verify_page(page)

    def test_basket_view(self):
        page = web.views.basket_view(dummy_func)()
        self._verify_page(page)

    def test_purchased_view(self):
        page = web.views.purchased_view(dummy_func)()
        self._verify_page(page)

    def test_report_view(self):
        page = web.views.report_view(dummy_func)()
        self._verify_page(page)
