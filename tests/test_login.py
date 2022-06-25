"""Testing the login page of saucedemo.com"""
import pytest
import test_data.login_creds as LoginCreds
from support.lib.constants import CHROME_DESKTOP, CHROME_HEADLESS, FIREFOX_DESKTOP, FIREFOX_HEADLESS
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*FIREFOX_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.STANDARD_PASSWORD)
        ,(*CHROME_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.STANDARD_PASSWORD)
    ],
)
@pytest.mark.login
@pytest.mark.login_success
@pytest.mark.high_priority
def test_login_valid_user(driver, browser, mode, device, username, password):
    """Test logging in with a valid username/password."""
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    assert not login_page.error_message_exists()
    print("Test finished.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*FIREFOX_HEADLESS, LoginCreds.LOCKED_OUT_USER, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.LOCKED_OUT_USER, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.smoke
def test_login_locked_out_user(driver, browser, mode, device, username, password):
    """Test logging in with a user who is locked out."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_locked_out_user finished successfully.")


@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*FIREFOX_HEADLESS, LoginCreds.STANDARD_USER, "abc123"),
        (*CHROME_HEADLESS, "notauser", LoginCreds.DROP_TABLES),
    ],
)
@pytest.mark.login
@pytest.mark.high_priority
@pytest.mark.smoke
def test_login_incorrect_credentials(driver, browser, mode, device, username, password):
    """Test attempting to reports in with invalid credentials."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_incorrect_credentials finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*FIREFOX_HEADLESS, LoginCreds.EMPTY_STRING, LoginCreds.STANDARD_PASSWORD),
        (*CHROME_HEADLESS, LoginCreds.EMPTY_STRING, LoginCreds.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.high_priority
def test_login_missing_username(driver, browser, mode, device, username, password):
    """Test attempting to reports in with a blank username."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_username finished successfully.")

@pytest.mark.parametrize(
    "browser,mode,device, username, password",
    [
        (*FIREFOX_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.EMPTY_STRING),
        (*CHROME_HEADLESS, LoginCreds.STANDARD_USER, LoginCreds.EMPTY_STRING),
    ],
)
@pytest.mark.login
def test_login_missing_password(driver, browser, mode, device, username, password):
    """Test attempting to reports in with a blank password."""
    login_page = LoginPage(driver)
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    print(login_page.get_error_message_text())
    print("test_login_missing_password finished successfully.")
