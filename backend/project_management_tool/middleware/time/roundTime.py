from datetime import datetime, timedelta


class roundTime:

    def round_to_quarter_hour(dt):
        # Calculate the minutes to the next quarter hour
        minutes_to_next_quarter = (15 - (dt.minute % 15)) % 15

        # Round the datetime to the next quarter hour
        rounded_datetime = dt + timedelta(minutes=minutes_to_next_quarter)

        return rounded_datetime