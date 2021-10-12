from copy import deepcopy
import lib.db


def _get_products_data(product_quantities, exclude_missing=True):
    """ inner join list of product IDs with product details """
    res = []
    for prod_id in product_quantities:
        qty = product_quantities[prod_id]
        if qty > 0 or not exclude_missing:
            prod = deepcopy(lib.db.PRODUCT_DATA[prod_id])
            prod['in_stock_quantity'] = qty
            res.append(prod)
    return res


def get_available_products():
    return _get_products_data(lib.db.AVAILABLE, exclude_missing=False)


def get_basket_products():
    return _get_products_data(lib.db.BASKET, exclude_missing=True)


def get_purchased_products():
    return _get_products_data(lib.db.PURCHASED, exclude_missing=True)


def add_to_basket(prod_id, qty=1):
    """ move 1 product from available list to the basket """
    lib.db.move(lib.db.AVAILABLE, lib.db.BASKET, prod_id, qty)


def remove_from_basket(prod_id, qty=1):
    lib.db.move(lib.db.BASKET, lib.db.AVAILABLE, prod_id, qty)


def purchase_basket():
    """ move all basket contents to 'purchased' """
    for id in lib.db.BASKET:
        lib.db.move(lib.db.BASKET, lib.db.PURCHASED, id, lib.db.BASKET[id])
