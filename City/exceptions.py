from rest_framework.exceptions import APIException


class CityNotFound(APIException):
    status_code = 404
    default_detail = 'City not found, try again.'
    default_code = 'City not found'
