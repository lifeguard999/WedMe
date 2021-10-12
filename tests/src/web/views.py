from bottle import jinja2_view
from web.bindings import get_available_products, get_basket_products, get_purchased_products

TEMPLATES_DIR = 'src/web/templates'

COLUMN_MAPPING = [
    {'label': 'ID', 'name': 'id', 'hidden': False, 'align': 'right'},
    {'label': 'Name', 'name': 'name', 'hidden': False, 'align': 'left'},
    {'label': 'Features', 'name': 'features', 'hidden': False, 'align': 'left'},
    {'label': 'Brand', 'name': 'brand', 'hidden': False, 'align': 'left'},
    {'label': 'Price', 'name': 'price_fmt', 'hidden': False, 'align': 'right'},
    {'label': 'Currency', 'name': 'currency', 'hidden': False, 'align': 'left'},
    {'label': 'Qty', 'name': 'in_stock_quantity', 'hidden': False, 'align': 'right'},
]


def _format_products_for_web(products):
    # sort rows by something reasonable:
    products.sort(key=lambda r: r['name'])
    # escaping
    pass  # it's in the templates
    return products


def gifts_view(func):
    """ Returns rendered page for gifts"""
    @jinja2_view('gifts.html', template_lookup=[TEMPLATES_DIR])
    def _gifts_view_call(*args, **kwargs):
        func(*args, **kwargs)
        return {'col_mapping': COLUMN_MAPPING,
                'product_list': _format_products_for_web(get_available_products())}
    return _gifts_view_call


def basket_view(func):
    """ Returns rendered page for basket """
    @jinja2_view('basket.html', template_lookup=[TEMPLATES_DIR])
    def _basket_view_call(*args, **kwargs):
        func(*args, **kwargs)
        return {'col_mapping': COLUMN_MAPPING, 'product_list': _format_products_for_web(get_basket_products())}
    return _basket_view_call


def purchased_view(func):
    """ Returns rendered 'purchased' page"""
    @jinja2_view('purchased.html', template_lookup=[TEMPLATES_DIR])
    def _purchased_view_call(*args, **kwargs):
        func(*args, **kwargs)
        return {'col_mapping': COLUMN_MAPPING, 'product_list': _format_products_for_web(get_purchased_products())}
    return _purchased_view_call


def report_view(func):
    """ Returns rendered report page """
    @jinja2_view('report.html', template_lookup=[TEMPLATES_DIR])
    def _report_view_call(*args, **kwargs):
        func(*args, **kwargs)
        return {'col_mapping': COLUMN_MAPPING,
                'basket_list': _format_products_for_web(get_basket_products()),
                'purchased_list': _format_products_for_web(get_purchased_products()),
                }
    return _report_view_call
