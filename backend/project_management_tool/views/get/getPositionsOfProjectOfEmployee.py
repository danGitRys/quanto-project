from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


@csrf_exempt
def getPositionsOfProjectOfEmployee(request,id,empId) -> JsonResponse:
    # Check if the request method is GET
    if request.method == "GET":
        # Decode JSON data from the request body

        with connection.cursor() as cursor:
            
            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            #
            sql_statement = """
                SELECT position.position_name, position.position_id, position.id FROM position
                INNER JOIN assignment ON position.fk_project = assignment.fk_project
                WHERE fk_employee = %s AND position.fk_project = %s;

            """
            cursor.execute(sql_statement, [empId,id])
            # Fetch the results
            result = [{"position_name":row[0], "position_id": row[1], "id": row[2]} for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"positions": result})