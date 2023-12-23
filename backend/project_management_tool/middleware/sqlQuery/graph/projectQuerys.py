from django.db import connection
class projectQuerys:

    def totalVolume(projectId:int):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(wd*rate*8) FROM position
                        WHERE fk_project = 1242
                        GROUP BY fk_project''',[projectId])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id = projectId
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
    
    def usedVolume(projectId:int):
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM(((DATEDIFF(MINUTE,booking.start,booking.[end])-booking.pause)/60)*position.rate) FROM booking
                            JOIN position ON position.id = booking.fK_position
                            JOIN project ON project.id = position.fk_project
                            WHERE  booking.fK_position IN (SELECT id FROM position WHERE fk_project=1242)''',[projectId])
        result = cursor.fetchall()
        print(result)
        print(len(result))
        if len(result) != 1:
            volume=0
            project_id = projectId
        else:
            volume = result[0]
        print("_-----------------------------")
        print(volume)
        print(result)
        return {
            'id':projectId,
            'volume':volume
        }
        