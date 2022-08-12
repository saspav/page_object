import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
LINK_PROMO = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f'{time.time()}@fakemail.org'
        password = f'{time.time()}_fake#pass'
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.user_can_add_product_to_basket()
        page.should_be_message_after_add_product()
        page.should_be_message_content_of_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK_PROMO)
    page.open()
    page.should_be_add_product_to_basket_button()
    page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_product()
    page.should_be_message_content_of_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK_PROMO)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()
    page.basket_should_be_empty_text()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# отметка упавшего теста
fail = 7
failed = pytest.param(f"{link_}?promo=offer{fail}",
                      marks=pytest.mark.xfail(reason="bag on page"))
urls = [f"{link_}?promo=offer{num}" if num != fail else failed
        for num in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_product()
    page.should_be_message_content_of_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_message()
