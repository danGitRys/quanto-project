from datetime import date,timedelta
class dateBack:

    def getDateWeeksBack(weeks:int):
        currentDate = date.today()
        days_ago = currentDate - timedelta(days=weeks*7)
        
        return days_ago


