from django.db import connection
class assignedProjects:

    def __init__(self,parameter:int) -> None:
        self.parameter = parameter
    
    def executeQuery(self):
        #TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT 
project.id,project.p_id,project.name,project.company,project.start_date,project.end_date,project.fk_creator,project.creation_date, 
assignment.id,assignment.fk_project,assignment.fk_employee,assignment.role
FROM project
JOIN assignment ON project.id = assignment.fk_project
WHERE assignment.fk_employee = %s''',[self.parameter])
        result = cursor.fetchall()
        print(result)
        # Convert the result to a list of dictionaries
        #result_list = [{'test': row[0]} for row in result]
        
        pass

    def toJsonTotal(self):
        #TODO implement
        pass
    