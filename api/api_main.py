# api/api_main.py
import requests

class UserAPI:
    BASE_URL = 'https://hr-challenge.dev.tapyou.com/api/test'

    @staticmethod
    def get_user_ids_by_gender(gender):
        response = requests.get(f"{UserAPI.BASE_URL}/users", params={'gender': gender})
        return response

    @staticmethod
    def get_user_info(user_id):
        response = requests.get(f"{UserAPI.BASE_URL}/user/{user_id}")
        return response