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
    # Evo go to main page
    browser.get(host)

    # He see the blackdog app title
    assert 'blackdog' in browser.title.lower()
    
    # He see 2 buttons to login and create new account
    assert browser.find_element_by_xpath('//button[normalize-space()="Sign in"]')
    assert browser.find_element_by_xpath('//button[normalize-space()="Sign up"]')


@pytest.mark.functional
def test_view_message_non_authorized(browser, host):
    """
    Mike is a new not authorized user.
    He was invited by Tom to his see his public message.
    """

    # Mike goes to link shared by Tom
    browser.get(host + '/tom/1')
    
    # TODO