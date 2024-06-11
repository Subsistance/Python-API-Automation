# test_user_api.py

import pytest
from api.api_main import UserAPI
from api.api_validation import (
    validate_user_ids_response,
    validate_invalid_user_ids_response,
    validate_user_info_response,
    validate_invalid_user_info_response
)

class TestUserAPI:

    @pytest.mark.parametrize("gender", ["male", "female"])
    def test_get_user_ids_by_gender(self, gender):
        response = UserAPI.get_user_ids_by_gender(gender)
        validate_user_ids_response(response)

    def test_get_user_ids_by_gender_invalid(self):
        response = UserAPI.get_user_ids_by_gender('unknown')
        validate_invalid_user_ids_response(response)

    def test_get_user_ids_by_empty_gender(self):
        response = UserAPI.get_user_ids_by_gender('')
        validate_invalid_user_ids_response(response)

    def test_get_user_info_valid(self):
        # Assuming 10 is a valid user ID
        response = UserAPI.get_user_info(10)
        validate_user_info_response(response)

    @pytest.mark.parametrize("user_id", ["99", "", "qwe"])
    def test_get_user_info_invalid(self, user_id):
        # Assuming 99 is an invalid user ID
        response = UserAPI.get_user_info(user_id)
        validate_invalid_user_info_response(response)