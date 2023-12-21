from datetime import datetime, timedelta
import random
class dateGenerator:

    def __init__(self,dayDiff:int) -> None:
        self.dayDiff = dayDiff

    def generateDate(self):
        pass

    def generateStartDate(self):
        # Set the time range
        start_time = datetime.strptime('08:00', '%H:%M')
        end_time = datetime.strptime('12:00', '%H:%M')

        # Calculate the time difference
        time_diff = end_time - start_time

        # Generate a random time within the time difference
        random_time = start_time + timedelta(minutes=random.randint(0, int(time_diff.total_seconds() / 60)))

        # Generate a random date within a reasonable range (e.g., last 30 days)
        random_date = datetime.now() + timedelta(days=self.dayDiff)

        # Combine the random date and time
        random_datetime = datetime.combine(random_date, random_time.time())

        return random_datetime
    def generateEndDate(self):
        # Set the time range
        start_time = datetime.strptime('14:00', '%H:%M')
        end_time = datetime.strptime('18:00', '%H:%M')

        # Calculate the time difference
        time_diff = end_time - start_time

        # Generate a random time within the time difference
        random_time = start_time + timedelta(minutes=random.randint(0, int(time_diff.total_seconds() / 60)))

        # Generate a random date within a reasonable range (e.g., last 30 days)
        random_date = datetime.now() + timedelta(days=self.dayDiff)

        # Combine the random date and time
        random_datetime = datetime.combine(random_date, random_time.time())

        return random_datetime
    
    def generatePauseTime(self,startDate:datetime,endDate:datetime):
         time_difference = endDate - startDate

        # Convert the timedelta to minutes
         time_difference_in_minutes = time_difference.total_seconds() / 60

         if time_difference_in_minutes <180:
             return 0

         else: 
             return 60
    
    def calculateTimeDifference(self,startDate:datetime,endDate:datetime):
         time_difference = endDate - startDate

        # Convert the timedelta to minutes
         time_difference_in_minutes = time_difference.total_seconds() / 60

         return time_difference_in_minutes

    

        