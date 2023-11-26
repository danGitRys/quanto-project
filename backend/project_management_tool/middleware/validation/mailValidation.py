import re

class MailValidator:

    @staticmethod
    def validate_mail(mail_string: str)->bool:
        """Function to check if the given string is a valid email-address

        Parameters
        ----------
        mail_string : str
            String to be validated

        Returns
        -------
        bool
            Result if the string matches the pattern
        """
        datetime_pattern = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
        return bool(datetime_pattern.match(mail_string))