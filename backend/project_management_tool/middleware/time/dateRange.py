import datetime
# Function definition

class dateRange:

    def range_date(start, end):
        res_date = start
        while res_date <= end:
            yield res_date
            res_date += datetime.timedelta(days=1)