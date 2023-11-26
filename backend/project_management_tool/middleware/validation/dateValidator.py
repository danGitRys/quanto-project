import re

class dateValidator:

    @staticmethod
    def validate_datetime(datetime_string: str)->bool:
        """Function to validate a given String against the pattern
        YYYY-MM-DD. Work from Year 1900 till 2099

        Parameters
        ----------
        datetime_string : str
            String to Validate

        Returns
        -------
        bool
            Result if String matches the given Pattern
        """
        datetime_pattern = re.compile(r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$")
        return bool(datetime_pattern.match(datetime_string))

    @staticmethod
    def validate_date(date_string: str)->bool:
        """Function to validate a given String against the pattern
        YYYY-MM-DD HH:MM:SS

        Parameters
        ----------
        date_string : str
            String to validate

        Returns
        -------
        bool
            Result if String matches the given Pattern
        """
        date_pattern = re.compile(r"^(?:(?:19|20)\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01])$")
        return bool(date_pattern.match(date_string))