from django.db import connection
class timeTable:

    def __init__(self,parameter:int) -> None:
        self.parameter = parameter
    
    def executeQuery(self):
        #TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT test FROM people_person''')
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries
        result_list = [{'test': row[0]} for row in result]
        
        pass

    def toJsonTotal(self):
        #TODO implement
        pass
    