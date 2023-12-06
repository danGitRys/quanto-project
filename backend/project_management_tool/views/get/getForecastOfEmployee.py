from django.http import JsonResponse
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json


@csrf_exempt
def getForecastOfEmployee(request, id) -> JsonResponse:
    # Check if the request method is POST
    if request.method == "GET":
        print("Hello World")
        # Decode JSON data from the request body

        with connection.cursor() as cursor:

            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            sql_statement = """
                SELECT *
                FROM forecast
                    WHERE fk_employee = %s;

            """
            cursor.execute(sql_statement, [id])
            # Fetch the results
            result = [{"id": row[0], "fk_employee": row[1], "fk_position": row[2],"start": row[3], "end": row[4], "info": row[5]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"forecast": result})
