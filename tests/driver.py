from selenium import webdriver


def get_local_driver():
    # if context.used_browser.lower() == "chrome":
    #     options = webdriver.ChromeOptions()
    #     if context.debug:
    #         options.add_experimental_option("detach", True)
    #     if context.headless:
    #         options.add_argument('--headless')

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # else:
    #     raise ValueError("Invalid used_browser")
    return driver
