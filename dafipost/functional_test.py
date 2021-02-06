from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.mark.functional
def test_home_title(browser):
    print(browser.title)
    assert 'dafipost' in browser.title
