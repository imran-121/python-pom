"""Constant variables used throughout the framework."""
from enum import Enum
from selenium import webdriver

class DriverPath():
    """Paths for the browser"""
    CHROME = "./support/drivers/chromedriver"
    FIREFOX = "./support/drivers/geckodriver"

class Mode(Enum):
    """Browsers modes used for test fixtures."""
    HEADLESS = "headless"
    DESKTOP = "desktop"

CHROME_DESKTOP = (webdriver.Chrome, Mode.DESKTOP, None)
CHROME_HEADLESS = (webdriver.Chrome, Mode.HEADLESS, None)
FIREFOX_DESKTOP = (webdriver.Firefox, Mode.DESKTOP, None)
FIREFOX_HEADLESS = (webdriver.Firefox, Mode.HEADLESS, None)
DEFAULT = CHROME_HEADLESS


