import re

class dateValidator:

    @staticmethod
    def validate_datetime(datetime_string: str):
        datetime_pattern = re.compile(r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$")
        return bool(datetime_pattern.match(datetime_string))

    @staticmethod
    def validate_date(date_string: str):
        date_pattern = re.compile(r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01])$")
        return bool(date_pattern.match(date_string))