from .cart import Cart


def cart(requset):
    cart = Cart(requset)
    return {'cart':cart}