from django.db import connection


class ProjectsFromEmployee:

    def __init__(self, parameter: int) -> None:
        self.parameter = parameter

    def executeQuery(self) -> list:
        # TODO implement
        cursor = connection.cursor()
        cursor.execute('''SELECT 
employee.id, employee.emp_id,employee.forename,employee.surname,employee.mail,employee.phone,employee.fk_team_id,employee.team_roll,
assignment.id,assignment.fk_project,assignment.fk_employee,assignment.role,
project.id, project.p_id,project.name,project.company,project.start_date,project.end_date,project.fk_creator,project.creation_date

FROM employee
JOIN assignment ON assignment.fk_employee = employee.id
JOIN project ON assignment.fk_project = project.id
WHERE employee.id = %s''', [self.parameter])
        result = cursor.fetchall()
        print(result)
        # Convert the result to a list of dictionaries
        # result_list = [{'test': row[0]} for row in result]

        return result

    def toJsonTotal(self) -> list:

        dbResult = self.executeQuery()
        result_list = [{'employee.id': row[0],
                        'employee.emp_id': row[1],
                        'employee.forename': row[2],
                        'employee.surname': row[3],
                        'employee.mail': row[4],
                        'employee.phone': row[5],
                        'employee.fk_team_id': row[6],
                        'employee.team_roll': row[7],
                        'assignment_id': row[8],
                        'assignment.fk_project': row[9],
                        'assignment.fk_employee': row[10],
                        'assignment_role': row[11],
                        'project.id': row[12],
                        
                        } for row in dbResult]
        return result_list
