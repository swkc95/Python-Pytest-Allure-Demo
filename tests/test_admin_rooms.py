from lib.pages import AdminLoginPage, AdminLayout, AdminRoomsPage
import lib.misc.variables as v
from lib.classes.class_room import Room
from lib.classes.class_api import APIRequests
import pytest
import allure


@allure.title("Admin adding and removing new rooms")
@allure.feature("Admin adding and removing new rooms")
@allure.tag("Admin")
@pytest.mark.admin
class TestAdminRooms:
    @allure.title("Admin creates a room with one additional feature")
    @allure.description("Admin logs in\n"
                        "Admin enters the rooms page\n"
                        "Admin provides a valid room info with type of <room_type>\n"
                        "Admin adds a room feature - <feature>\n"
                        "Admin sends a new room form\n"
                        "Admin sees the new room on the rooms list\n"
                        "[API] New room is present in the database")
    @allure.testcase("TC-3")
    @pytest.mark.parametrize("room_type,feature", [("Single", "WiFi"), ("Single", "Radio")])
    def test_admin_create_room_with_feature(self, browser, room_type, feature):
        # Admin logs in
        page = AdminLoginPage(browser)
        page.visit()
        page.banner_button.click()
        page.login(v.ADMIN_USERNAME, v.ADMIN_PASSWORD)

        # Admin enters the rooms page
        page = AdminLayout(browser)
        page.rooms_tab.click()

        # Admin provides a valid room info with type of <room_type>
        page = AdminRoomsPage(browser)
        room = Room()
        room.type = room_type
        page.fill_room_form(room)

        # Admin adds a room feature - <feature>
        room.features = [feature]
        page.add_room_features(room)

        # Admin sends a new room form
        page.create_button.click()

        # Admin sees the new room on the rooms list
        page.set_format_variable(room.number)
        new_room = page.room_entry_by_room_number.text
        assert room.type in new_room
        assert str(room.is_accessible).lower() in new_room
        assert room.price in new_room
        assert all(element in new_room for element in room.features)

        # [API] New room is present in the database
        rooms = APIRequests.get_rooms()
        assert f'"roomName":"{room.number}"' in rooms

    @allure.title("Admin deletes a room")
    @allure.description("[API] New random room added\n"
                        "Admin logs in\n"
                        "Admin enters the rooms page\n"
                        "Admin finds newly added room and deletes it\n"
                        "Admin does not see the new room on the rooms list\n"
                        "[API] Deleted room is not present in the database")
    @allure.testcase("TC-4")
    def test_admin_delete_room(self, browser):
        # [API] New random room added
        room = Room()
        APIRequests.create_room(room)

        # Admin logs in
        page = AdminLoginPage(browser)
        page.visit()
        page.banner_button.click()
        page.login(v.ADMIN_USERNAME, v.ADMIN_PASSWORD)

        # Admin enters the rooms page
        page = AdminLayout(browser)
        page.rooms_tab.click()

        # Admin finds newly added room and deletes it
        page = AdminRoomsPage(browser)
        page.delete_room(room)

        # Admin does not see the new room on the rooms list
        assert room.number not in page.room_table.text

        # [API] Deleted room is not present in the database
        rooms = APIRequests.get_rooms()
        assert f'"roomName":"{room.number}"' not in rooms
