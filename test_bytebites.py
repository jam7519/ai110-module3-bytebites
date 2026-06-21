from models import MenuItem, Menu, Order


def test_order_total():
    burger = MenuItem("Burger", 10.0, "Food", 5)
    soda = MenuItem("Soda", 5.0, "Drink", 4)

    order = Order()
    order.add_item(burger)
    order.add_item(soda)

    assert order.calculate_total() == 15.0


def test_empty_order_total():
    order = Order()

    assert order.calculate_total() == 0


def test_filter_by_category():
    burger = MenuItem("Burger", 10.0, "Food", 5)
    soda = MenuItem("Soda", 5.0, "Drink", 4)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    drinks = menu.filter_by_category("Drink")

    assert len(drinks) == 1
    assert drinks[0].name == "Soda"

    