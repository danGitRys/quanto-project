
from dateutil import parser
class dateValidator:

    def date(dateString:str):
        format = "YYYY-MM-DD"
        result = True
        try:
            result = bool(parser.parse(dateString))
        except ValueError:
            result = False