import re
from datetime import datetime,timedelta
import json
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
    
    def validateBookingTimes(startTime:str,endTime:str,pause:str)->json:
        date_format = "%Y-%m-%d %H:%M:%S"
        start_datetime = datetime.strptime(startTime,date_format)
        end_datetime = datetime.strptime(endTime,date_format)
        dateOrder:bool = start_datetime<end_datetime
        if dateOrder:
            timeDifference:timedelta = (end_datetime-start_datetime)
            timeDifferenceMinutes = timeDifference.total_seconds()
            if timeDifferenceMinutes>int(pause)*60:
                return {
                    "valid":True,
                    "errors":[]
                }
            else:
                return{
                    "valid": False,
                    "errors": ["Pause longer then working time"]
                }


        else:
            return {
                "valid":False,
                "errors":["Endtime before StartTime"]
            }




