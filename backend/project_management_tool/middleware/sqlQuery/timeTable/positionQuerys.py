from django.db import connection

class positionQuerys:

    def forecastTimeForDate(positionId:int,employeeId:int,date):
            cursor = connection.cursor()
            cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,forecast.start,forecast.[end])))) FROM forecast
        JOIN position ON position.id = forecast.fK_position
        JOIN project ON project.id = position.fk_project
        WHERE  forecast.fK_position =%s AND fk_employee=%s AND CONVERT(DATE,forecast.start) = %s
            ''',[positionId,employeeId,date])
            result = cursor.fetchall()
            #print(result)
            #print(len(result))
            if len(result) != 1:
                volume=0
                position_id=positionId
            else:
                volume = result[0]
            #print("_-----------------------------")
            #print(volume)
            #print(result)
            # Convert the result to a list of dictionaries
            #result_list = [{'test': row[0]} for row in result]
            
            return {
                'id':positionId,
                'volume':volume
            }


