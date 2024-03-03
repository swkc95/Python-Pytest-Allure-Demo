import os
import pytest
import allure
from selenium import webdriver
from lib.misc.string_importer import import_string_file
from datetime import datetime


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    _browser = webdriver.Chrome(options=options)
    _browser.maximize_window()
    yield _browser
    _browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        browser = item.funcargs['browser']
        screenshot_path = f"fail_{item.name}{date}.png"
        browser.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
        os.remove(screenshot_path)


@pytest.fixture()
def strings():
    _strings = import_string_file("english")
    return _strings
