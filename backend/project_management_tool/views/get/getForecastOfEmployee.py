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

            ## end reserviertes Schlüsselwort daher in eckickge Klammern!!!
            sql_statement = """
                SELECT forecast.id, forecast.fk_employee, forecast.fk_position, forecast.start,forecast.[end],forecast.info, DATEDIFF(HOUR,forecast.start, forecast.[end]) AS duration, CONVERT(VARCHAR(10), forecast.start,104) AS date,position.position_id, DATEDIFF(HOUR, booking.start, booking.[end]) AS time_difference
                FROM forecast
                INNER JOIN position AS position ON forecast.fk_position = position.id
                INNER JOIN booking ON booking.fK_position = position.id
                WHERE forecast.fk_employee = %s;

            """
            cursor.execute(sql_statement, [id])
            # Fetch the results
            result = [{"id": row[0], "fk_employee": row[1], "fk_position": row[2], "start": row[3], "end": row[4], "info": row[5], "duration": row[6], "date": row[7], "positionName": row[8], "worked": row[9]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"forecast": result})
