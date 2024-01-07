from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


@csrf_exempt
def getAllPositionsFromAllProjects(request, id) -> JsonResponse:
    # Check if the request method is POST
    if request.method == "GET":
        # Decode JSON data from the request body

        with connection.cursor() as cursor:

            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            #
            sql_statement = """
                SELECT position.position_id, position.id,pro.name FROM position
                JOIN assignment ON position.fk_project = assignment.fk_project
				JOIN project AS pro ON pro.id = assignment.fk_project 
                WHERE fk_employee = %s
               
            """
            cursor.execute(sql_statement, [id])
            # Fetch the results
            result = [{"position_id": row[0], "id": row[1], "projectName": row[2]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"positions": result})
