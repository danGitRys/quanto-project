from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def getProjectsOfEmployee(request, id) -> JsonResponse:
 
    if request.method == "GET":

        with connection.cursor() as cursor:
            
            sql_statement = """
                SELECT project.name, project.id 
                FROM project
                INNER JOIN assignment ON project.id = assignment.fk_project
                WHERE assignment.fk_employee = %s
            """
            cursor.execute(sql_statement, [id])
            
            result = [{"name": row[0], "id": row[1]} for row in cursor.fetchall()]
            
        # Process 'result' and return JsonResponse
        return JsonResponse({"projects": result})
    else:
        # Return an error response for non-POST requests
        return JsonResponse({"error": "Invalid request method"}, status=400)
