import re
class dateValidator:

    @staticmethod
    def validate(dateString: str):
        date_pattern = re.compile(r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01])$")
        return bool(date_pattern.match(dateString))