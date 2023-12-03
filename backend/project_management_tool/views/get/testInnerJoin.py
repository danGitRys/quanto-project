from django.http import JsonResponse
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


@csrf_exempt
def testInnerJoin(request, id) -> JsonResponse:
    # Check if the request method is POST
    if request.method == "GET":
        print("Hello World")
        # Decode JSON data from the request body

        with connection.cursor() as cursor:
            # SQL statement with a placeholder for employee_id
            sql_statement = """
                SELECT project.name, project.id 
                FROM project
                INNER JOIN assignment ON project.id = assignment.fk_project
                WHERE assignment.fk_employee = %s
            """
            cursor.execute(sql_statement, [id])
            # Fetch the results
            result = [{"name": row[0], "id": row[1]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"projects": result})
    else:
        # Return an error response for non-POST requests
        return JsonResponse({"error": "Invalid request method"}, status=400)
