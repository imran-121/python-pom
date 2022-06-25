#!/usr/bin/env python

import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from support.lib.constants import Mode, DriverPath
from selenium.webdriver.firefox.options import Options

"""Defining actions to be executed before and after test case execution"""
@pytest.fixture
def driver(request, browser, mode, device):
    if browser == webdriver.Chrome:
        if mode == Mode.DESKTOP:
            options = webdriver.ChromeOptions()
            web_driver = browser(DriverPath.CHROME, options=options)
        elif mode == Mode.HEADLESS:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            web_driver = browser(DriverPath.CHROME, options=options)
        else:
            web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == webdriver.Firefox:
        if mode == Mode.DESKTOP:
            web_driver = webdriver.Firefox(executable_path=DriverPath.FIREFOX)
        elif mode == Mode.HEADLESS:
            options = Options()
            options.headless = True
            web_driver = webdriver.Firefox(executable_path=DriverPath.FIREFOX,options=options)
    else:
        raise NameError("Unsupported browser: %s" % browser)

    web_driver.delete_all_cookies()

    # Close/quit browser after the test is completed.
    request.addfinalizer(lambda *args: mac_finalizer(web_driver))
    return web_driver


def mac_finalizer(web_driver):
    """Close/quit browser after the test is completed."""
    web_driver.close()
    web_driver.quit()
    time.sleep(2)
