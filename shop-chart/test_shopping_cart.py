from shopping_cart import ShoppingCart
import pytest

max_size = 5


def test_can_add_item_to_cart():
    cart = ShoppingCart(max_size)
    cart.add('apple')
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(max_size)
    cart.add('apple')
    assert 'apple' in cart.get_items()


def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(max_size)
    for _ in range(max_size):
        cart.add('apple')

    with pytest.raises(OverflowError):
        cart.add('apple')


def test_can_get_total_price():
    cart = ShoppingCart(2)
    cart.add('apple')
    cart.add('milk')

    prince_map = {
        'apple': 1.0,
        'milk': 2.0,
    }
    assert cart.get_total_price(prince_map) == 3.0
