import requests
import lib.misc.variables as v


class APIRequests:
    token = ""

    @classmethod
    def get_auth_token(cls):
        body = {
            "username": v.ADMIN_USERNAME,
            "password": v.ADMIN_PASSWORD
        }

        response = requests.post(url=v.API_URL + v.API_AUTH_ENDPOINT, json=body)
        if response.status_code != 200:
            raise requests.RequestException("API get_auth_token has failed")
        cls.token = response.cookies["token"]

    @classmethod
    def check_auth_token(cls):
        if not cls.token:
            cls.get_auth_token()
        return cls.token

    @classmethod
    def create_room(cls, room):
        cookies = {
            "token": cls.check_auth_token()
        }

        body = {
            "roomid": room.id,
            "roomName": room.number,
            "type": room.type,
            "accessible": room.is_accessible,
            "image": room.image,
            "description": room.description,
            "features": room.features,
            "roomPrice": room.price
        }

        response = requests.post(url=v.API_URL + v.API_ROOM_ENDPOINT, json=body, cookies=cookies)
        if response.status_code != 201:
            raise requests.RequestException("API create_room has failed")

    @classmethod
    def delete_room(cls, room):
        headers = {
            "id": room.id
        }

        response = requests.delete(url=v.API_URL + v.API_ROOM_ENDPOINT, headers=headers)
        if response.status_code != 200:
            raise requests.RequestException("API delete_room has failed")

    @classmethod
    def get_bookings(cls):
        cookies = {
            "token": cls.check_auth_token()
        }

        response = requests.get(url=v.API_URL + v.API_BOOKING_ENDPOINT, cookies=cookies)
        if response.status_code != 200:
            raise requests.RequestException("API get_bookings has failed")
        return response.text

    @classmethod
    def get_rooms(cls):
        response = requests.get(url=v.API_URL + v.API_ROOM_ENDPOINT)
        if response.status_code != 200:
            raise requests.RequestException("API get_rooms has failed")
        return response.text

    @classmethod
    def get_messages(cls):
        response = requests.get(url=v.API_URL + v.API_MESSAGES_ENDPOINT)
        if response.status_code != 200:
            raise requests.RequestException("API get_messages has failed")
        return response.text
