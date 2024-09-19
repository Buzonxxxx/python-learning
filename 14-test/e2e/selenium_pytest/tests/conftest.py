import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from selenium import webdriver
from selenium_pytest.utils.config_reader import get_config

@pytest.fixture(scope="session")
def config():
    return get_config()

@pytest.fixture(scope="function")
def driver(config):
    browser = config['DEFAULT']['browser']
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.implicitly_wait(int(config['DEFAULT']['implicit_wait']))
    driver.get(config['DEFAULT']['base_url'])
    yield driver
    driver.quit()