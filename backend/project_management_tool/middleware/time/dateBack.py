from datetime import date,timedelta
class dateBack:

    def getDateWeeksBack(weeks:int):
        currentDate = date.today()
        days_ago = currentDate - timedelta(days=weeks*7)
        formatted_days_ago = days_ago.strftime("%Y-%m-%d")
        return formatted_days_ago


