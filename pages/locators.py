﻿from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_AFTER_ADD = (By.CSS_SELECTOR, "div.alertinner")
    MESSAGE_CONTENT_BASKET = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasketPageLocators:
    EMPTY_BUSKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_IN_BUSKET = (By.CSS_SELECTOR, ".basket_summary")
