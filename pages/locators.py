from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    GOOD = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    ADDING_GOODS_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_CHECK = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRICE_CHECK = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
