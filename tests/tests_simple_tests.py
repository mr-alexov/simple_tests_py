from selene import browser, have


def test_the_internent_heroku_login(get_browser):
    browser.open('https://the-internet.herokuapp.com/login')
    browser.element("#username").type("tomsmith")
    browser.element("#password").type("SuperSecretPassword!")
    browser.element("button[type='submit']").click()

    browser.element("h2").should(have.text("Secure Area"))
