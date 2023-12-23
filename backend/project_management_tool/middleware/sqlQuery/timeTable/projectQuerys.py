from django.db import connection
class projectQuerys:

    def timeInProjectBookedDay(projectId:int,employeeId:int,date):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause))) FROM booking
        JOIN position ON position.id = booking.fK_position
        JOIN project ON project.id = position.fk_project
        WHERE  booking.fK_position IN (SELECT id FROM position WHERE fk_project=%s) AND fk_employee=%s AND CONVERT(DATE,booking.start) = %s
        ''',[projectId,employeeId,date])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id=projectId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':projectId,
            'volume':volume
        }

    def timeNotInProjectBookedDay(projectId:int,employeeId:int,date):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause))) FROM booking
        JOIN position ON position.id = booking.fK_position
        JOIN project ON project.id = position.fk_project
        WHERE  booking.fK_position NOT IN (SELECT id FROM position WHERE fk_project=%s) AND fk_employee=%s AND CONVERT(DATE,booking.start) = %s
        ''',[projectId,employeeId,date])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id=projectId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':projectId,
            'volume':volume
        }
    
    def timeInProjectForecastDay(projectId:int,employeeId:int,date):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,forecast.start,forecast.[end])))) FROM forecast
        JOIN position ON position.id = forecast.fK_position
        JOIN project ON project.id = position.fk_project
        WHERE  forecast.fK_position IN (SELECT id FROM position WHERE fk_project=%s) AND fk_employee=%s AND CONVERT(DATE,forecast.start) = %s

        ''',[projectId,employeeId,date])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id=projectId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':projectId,
            'volume':volume
        }
    
    def timeNotInProjectForecastDay(projectId:int,employeeId:int,date):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,forecast.start,forecast.[end])))) FROM forecast
        JOIN position ON position.id = forecast.fK_position
        JOIN project ON project.id = position.fk_project
        WHERE  forecast.fK_position NOT IN (SELECT id FROM position WHERE fk_project=%s) AND fk_employee=%s AND CONVERT(DATE,forecast.start) = %s

        ''',[projectId,employeeId,date])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id=projectId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':projectId,
            'volume':volume
        }

    
