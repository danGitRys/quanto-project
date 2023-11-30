from django.db import connection
class assignedProjects:

    def __init__(self,parameter:int) -> None:
        self.parameter = parameter
    
    def executeQuery(self)->list:
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
        
        return result

    def toJsonTotal(self)->list:
        #TODO implement
        dbResult = self.executeQuery()
        result_list = [{'project_id': row[0],
                        'project_pid':row[1],
                        'project_name':row[2],
                        'project_company':row[3],
                        'project_start_date':row[4],
                        'project_end_date':row[5],
                        'project_creator':row[6],
                        'creation_date':row[7],
                        'assignment_id':row[8],
                        'assignment_project_id':row[9],
                        'assignment_employee_id':row[10],
                        'assignment_role':row[11]
                        } for row in dbResult]
        return result_list
    