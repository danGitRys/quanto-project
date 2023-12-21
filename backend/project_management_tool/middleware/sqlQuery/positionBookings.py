from django.db import connection
class positionBookings:

    def __init__(self,date,project_id) -> None:
        self.date = date
        self.project_id = project_id
    
    def executeQuery(self)->list:
        #TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT position.id, SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause)/60)*position.rate) FROM booking
                        JOIN position ON position.id = booking.fK_position
                        JOIN project ON project.id = position.fk_project
                        WHERE CONVERT(DATE,booking.start) = %s AND booking.fK_position=%s
                        GROUP BY position.id''',[self.date,self.project_id])
        result = cursor.fetchall()
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return result

    def toJsonTotal(self)->list:

        dbResult = self.executeQuery()
        result_list = [{'project_id': row[0],
                        'volume':row[1],
                        } for row in dbResult]
        return result_list