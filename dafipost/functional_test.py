"""
User stories as a bunch of functional tests in a real webdriver.
"""

from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.fixture
def host():
    return 'http://localhost:8000'


@pytest.mark.functional
def test_index_non_authorized(browser, host):
    """
    Evo is here for the first time and wants to give a try to our application.
    """
    # Evo goes to home page
    browser.get(host)

    # He see the blackdog app title
    assert 'dafipost' in browser.title.lower()
    
    # He see 2 buttons to login and create new account
    assert browser.find_element_by_xpath("//*[contains(text(), 'Sign up')]")
