import allure
from selene import browser, have, be


def test_the_internent_heroku_login(get_browser):
    with allure.step("Открыть страницу логина на the-internet.herokuapp и залогиниться"):
        browser.open('https://the-internet.herokuapp.com/login')
        browser.element("#username").type("tomsmith")
        browser.element("#password").type("SuperSecretPassword!")
        browser.element("button[type='submit']").click()
    with allure.step("Проверить что залогинились"):
        browser.element("h2").should(have.text("Secure Area"))


def test_magento_stb_search(get_browser):
    with allure.step("Открыть страницу Magento STB"):
        browser.open('https://magento.softwaretestingboard.com/')
    with allure.step("Сделать поиск 'pants'"):
        browser.element("#search").type("pants")
        browser.element("#search").press_enter()

    with allure.step("Проверить наличие Pant в поисковой выдаче"):
        browser.element(".product-item-link").should(be.visible)
        browser.element(".product-item-link").should(have.text("Pant"))
