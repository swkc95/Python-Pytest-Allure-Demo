from selenium.webdriver.common.by import By
from lib.pages.page_admin_layout import AdminLayout


class AdminRoomsPage(AdminLayout):
    def __init__(self, browser):
        super().__init__(browser)
        self.site_url = "/#/admin"
        self.locator_dictionary.update(self.page_locator_dictionary)

    page_locator_dictionary = {
        "delete_button_by_room_id": (By.XPATH, '//p[@id="roomName{}"]/..//following-sibling::div/span'),
        "room_entry_by_room_number": (By.XPATH, '//p[@id="roomName{}"]/../..'),
        "room_table": (By.XPATH, '//p[contains(text(), "Room #")]/../../..'),
        "room_number_field": (By.CSS_SELECTOR, '#roomName'),
        "room_type_list": (By.CSS_SELECTOR, '#type'),
        "room_type_pick": (By.XPATH, '//select[@id="type"]/option[@value="{}"]'),
        "room_accessibilty_list": (By.CSS_SELECTOR, '#accessible'),
        "room_accessibility_pick": (By.XPATH, '//select[@id="accessible"]/option[@value="{}"]'),
        "room_price_field": (By.CSS_SELECTOR, '#roomPrice'),
        "wifi_checkbox": (By.CSS_SELECTOR, '#wifiCheckbox'),
        "tv_checkbox": (By.CSS_SELECTOR, '#tvCheckbox'),
        "radio_checkbox": (By.CSS_SELECTOR, '#radioCheckbox'),
        "refreshments_checkbox": (By.CSS_SELECTOR, '#refreshCheckbox'),
        "safe_checkbox": (By.CSS_SELECTOR, '#safeCheckbox'),
        "views_checkbox": (By.CSS_SELECTOR, '#viewsCheckbox'),
        "create_button": (By.CSS_SELECTOR, '#createRoom'),
        "validation_field": (By.CSS_SELECTOR, '.alert.alert-danger')
    }

    def delete_room(self, room):
        self.find_element("delete_button_by_room_id", frmt=room.number).click()
        self.wait_for_invisibility("room_entry_by_room_number", frmt=room.number)

    def fill_room_form(self, room):
        self.find_element("room_number_field").send_keys(room.number)
        self.find_element("room_price_field").send_keys(room.price)
        self.find_element("room_type_list").click()
        self.find_element("room_type_pick", frmt=room.type).click()
        self.find_element("room_accessibilty_list").click()
        self.find_element("room_accessibility_pick", frmt=str(room.is_accessible).lower()).click()

    def add_room_features(self, room):
        for feature in room.features:
            self.find_element(f"{feature.lower()}_checkbox").click()
