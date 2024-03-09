import os
import pytest
import allure
from selenium import webdriver
from lib.misc.string_importer import import_string_file
from datetime import datetime


@pytest.fixture
def browser(request):
    debug_mode = request.config.getoption("--test-debug")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", not debug_mode)
    if not debug_mode:
        options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser
    if not debug_mode:
        browser.quit()


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


@pytest.fixture
def strings(request):
    language = request.config.getoption("--lang")
    strings = import_string_file(language)
    return strings


def pytest_addoption(parser):
    parser.addoption("--lang", action="store", default="english", help="Choose language strings")
    parser.addoption("--test-debug", action="store_true", default=False,
                     help="Debug mode - visible browser, stays open after the test")
