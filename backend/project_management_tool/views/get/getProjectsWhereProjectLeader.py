from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json

@csrf_exempt
def getProjectsWhereProjectLeader(request, id) -> JsonResponse:
    # Check if the request method is POST
    if request.method == "GET":
        # Decode JSON data from the request body

        with connection.cursor() as cursor:

            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            #
            sql_statement = """
                SELECT pro.name AS projectName ,ass.fk_project AS forgeinKeyProject FROM assignment AS ass
                JOIN project AS pro ON pro.id = ass.fk_project
                WHERE ass.fk_employee = %s AND ass.role = 'ProjectLeader'

            """
            cursor.execute(sql_statement, [id])
            # Fetch the results
            result = [{"projectNames": row[0], "foreignKeysForProject": row[1]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"projects": result})
