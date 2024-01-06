from django.db import connection
class eligiblePositionIds:

    def __init__(self,parameter:int) -> None:
        self.parameter = parameter
    
    def executeQuery(self)->list:
        #TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT position.id FROM position
JOIN project ON project.id = position.fk_project
JOIN assignment ON assignment.fk_project = project.id
JOIN employee ON employee.id = assignment.fk_employee
WHERE employee.id
 = %s''',[self.parameter])
        result = cursor.fetchall()
        #print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        return result

    def toJsonTotal(self)->list:

        dbResult = self.executeQuery()
        result_list = [{'position_id': row[0]
                        } for row in dbResult]
        return result_list