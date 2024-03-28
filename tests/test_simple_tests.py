from selene import browser, have, be


def test_the_internent_heroku_login(get_browser):
    browser.open('https://the-internet.herokuapp.com/login')
    browser.element("#username").type("tomsmith")
    browser.element("#password").type("SuperSecretPassword!")
    browser.element("button[type='submit']").click()

    browser.element("h2").should(have.text("Secure Area"))


def test_magento_stb_search(get_browser):
    browser.open('https://magento.softwaretestingboard.com/')
    browser.element("#search").type("pants")
    browser.element("#search").press_enter()
    browser.element(".product-item-link").should(be.visible)

    browser.element(".product-item-link").should(have.text("Pant"))
