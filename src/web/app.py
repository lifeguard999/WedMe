import bottle
import lib.db
import web.bindings
import web.views


# Gifts page

@bottle.route('/')
@web.views.gifts_view
def index():
    pass


@bottle.route('/tobasket/<prod_id>')
@web.views.gifts_view
def tobasket(prod_id):
    web.bindings.add_to_basket(int(prod_id))


# Basket page

@bottle.route('/basket')
@web.views.basket_view
def basket():
    pass


@bottle.route('/frombasket/<prod_id>')
@web.views.basket_view
def frombasket(prod_id):
    web.bindings.remove_from_basket(int(prod_id))


@bottle.route('/purchase')
@web.views.purchased_view
def purchase():
    web.bindings.purchase_basket()


# Purchased page

@bottle.route('/purchased')
@web.views.purchased_view
def purchased():
    pass


# Report page

@bottle.route('/report')
@web.views.report_view
def report():
    pass


def main():
    lib.db.init()
    bottle.run(host='localhost', port=8080, debug=True, reloader=True)


if __name__ == '__main__':
    main()
