# api/api_validation.py
import pytest_check as check

# Using some default values in all methods in case of missing fields
def validate_user_ids_response(response):
    check.equal(response.status_code, 200)
    data = response.json()
    check.equal(data.get('success', False), True)
    check.equal(data.get('errorCode', -1), 0)
    check.is_none(data.get('errorMessage', None))
    check.is_instance(data.get('result', ""), list)

def validate_invalid_user_ids_response(response):
    check.equal(response.status_code, 400)
    data = response.json()
    check.equal(data.get('success', True), False)
    check.equal(data.get('errorCode', -1), 400)
    check.is_not_none(data.get('errorMessage', "default error message"))

def validate_user_info_response(response):
    check.equal(response.status_code, 200)
    data = response.json()
    check.equal(data.get('success', False), True)
    check.equal(data.get('errorCode', -1), 0)
    check.is_none(data.get('errorMessage', None))
    check.is_instance(data.get('result', ""), dict)
    for field in ['id', 'name', 'gender', 'age', 'city', 'registrationDate']:
        check.is_in(field, data['result'])

def validate_invalid_user_info_response(response):
    check.equal(response.status_code, 400)
    data = response.json()
    check.equal(data.get('success', True), False)
    check.equal(data.get('errorCode', -1), 400)
    check.is_not_none(data.get('errorMessage', "default error message"))