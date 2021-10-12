"""
Fast, in-memory DB ;)
"""
import json
from lib.utils import get_abs_path, fmt_price

# product table, loaded form JSON file
PRODUCTS_FILE = 'etc/products.json'
PRODUCT_DATA = {}

# below map product ID to quantity:
# Id -> Qty
AVAILABLE = {}
BASKET = {}
PURCHASED = {}


def move(src, target, prod_id, qty):
    """ move products between AVAILABLE, BASKET and PURCHASED """
    if src.get(prod_id, 0) >= qty:
        src[prod_id] = src[prod_id] - qty
        target[prod_id] = target.get(prod_id, 0) + qty


def init():
    """
        Init the in-memory DB.
        Loads JSON file, resets product counters
    """
    products = _load_products_list()
    BASKET.clear()
    PURCHASED.clear()
    AVAILABLE.clear()
    for product in products:
        id = product['id']
        qty = product['in_stock_quantity']
        AVAILABLE[id] = qty
        PRODUCT_DATA[id] = product
    if len(products) != len(AVAILABLE):
        raise RuntimeError('Could not init product database due to duplicate IDs')


def _load_products_list():
    """ Loads products.json file and returns as dict """
    products_json_path = get_abs_path(PRODUCTS_FILE)
    with open(products_json_path, 'r') as f:
        products_list = json.load(f)
    for product in products_list:
        # split price & ccy:
        product['currency'] = product['price'][-3:]
        product['price'] = float(product['price'][:-3])
        product['price_fmt'] = fmt_price(product['price'])
        # correct case:
        product['brand'] = product['brand'].title()
        # extract features from name:
        name = product['name']
        name_parts = name.replace(';', ',').split(',')
        product['name'] = name_parts[0]
        product['features'] = ', '.join([name.strip() for name in name_parts[1:]])
    return products_list
