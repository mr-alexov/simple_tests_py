import pytest
from selene.support.shared import browser


@pytest.fixture
def get_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('about:blank')
    yield
