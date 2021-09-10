from rest_framework.exceptions import APIException


class UserEmailNotFound(APIException):
    status_code = 409
    default_detail = 'For a successful subscription and further mailing,' \
                     ' you must fill in the email field.'
    default_code = 'User email not found'
