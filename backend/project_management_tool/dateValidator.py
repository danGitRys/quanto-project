
from dateutil import parser
class dateValidator:

    def date(dateString:str)->bool:
        """Function to validate if the given String is a valid Date
        in the Format YYYY--MM-DD

        Parameters
        ----------
        dateString : str
            _description_

        Returns
        -------
        bool
            _description_
        """
        format = "YYYY-MM-DD"
        result = True
        try:
            result = bool(parser.parse(dateString))
        except ValueError:
            result = False
        return result