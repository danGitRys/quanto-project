from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def getBookingTimes(request, id, currentDay) -> JsonResponse:
    # Check if the request method is GET
    if request.method == "GET":
        with connection.cursor() as cursor:
            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            sql_statement = """
            
                SELECT CONVERT(TIME, booking.start) AS start_time, CONVERT(TIME, booking.[end]) AS end_time, pause,  CONVERT(TIME, f.start) AS forecast_start , CONVERT(TIME, f.[end]) AS forcast_end
                FROM booking
                JOIN forecast AS f ON f.fk_position = booking.fK_position
                WHERE f.fk_position = %s AND CAST(f.start AS DATE) = CONVERT(date, %s, 104)
                AND CAST(booking.start AS DATE) = CONVERT(date, %s, 104);

        
            """
            cursor.execute(sql_statement, [id, currentDay, currentDay])
            # Fetch the results
            result = [{"start_time": row[0], "end_time": row[1], "pause": row[2], "forecast_start": row[3], "forecast_end": row[4]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"bookingTimes": result})
