from django.db import connection
class positionQuerys:

    def totalVolume(positionId:int):
        cursor = connection.cursor()
        cursor.execute('''SELECT wd*rate*8 FROM position
                        WHERE id = %s''',[positionId])
        result = cursor.fetchall()
        #print(result)
        #print(len(result))
        if len(result) != 1:
            volume=0
            position_id=positionId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':positionId,
            'volume':volume
        }
    
    def usedVolume(positionId:int):
        cursor = connection.cursor()
        cursor.execute('''SELECT position.id, SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause)/60)*position.rate) FROM booking
                        JOIN position ON position.id = booking.fK_position
                        JOIN project ON project.id = position.fk_project
                        WHERE  booking.fK_position=%s
                        GROUP BY position.id''',[positionId])
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
        return {
            'id':positionId,
            'volume':volume
        }
    
    def usedVolumeOnDay(date,positionId)->list:
        #TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT position.id, SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause)/60)*position.rate) FROM booking
                        JOIN position ON position.id = booking.fK_position
                        JOIN project ON project.id = position.fk_project
                        WHERE CONVERT(DATE,booking.start) = %s AND booking.fK_position=%s
                        GROUP BY position.id''',[date,positionId])
        result = cursor.fetchall()
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id=0
        else:
            project_id, volume = result[0]
        #print("_-----------------------------")
        #print(volume)
        #print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return {
            'id':project_id,
            'volume':volume
        }

        
