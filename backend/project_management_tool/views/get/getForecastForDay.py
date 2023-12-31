from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def getForecastForDay(request, id, currentDay) -> JsonResponse:
    # Check if the request method is GET
    if request.method == "GET":
        with connection.cursor() as cursor:
            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            sql_statement = """
            
                SELECT CONVERT(TIME, f.start) AS forecast_start , CONVERT(TIME, f.[end]) AS forcast_end,
                f.fk_position AS position_id
                FROM forecast AS f
                WHERE f.fk_position = %s AND CAST(f.start AS DATE) = CONVERT(date, %s, 104)
                

        
            """
            cursor.execute(sql_statement, [id, currentDay])
            # Fetch the results
            result = [{"forecast_start": row[0], "forecast_end": row[1], "position_id": row[2]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"forecastTimes": result})
