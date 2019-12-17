import pytest
from .pages.product_page import ProductPage


product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_link}/?promo=offer{no}" for no in range(10)]
urls[7] = pytest.param("7", marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.solve_quiz_and_get_code()
    cart.price_correct()
    cart.items_correct()
