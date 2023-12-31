from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def getBookingTimesForDay(request, id, currentDay) -> JsonResponse:
    # Check if the request method is GET
    if request.method == "GET":
        with connection.cursor() as cursor:
            # DIE 8 MUSS NOCH ERSETZT WERDEN DURCH EMPLOYEE_ID, PFAD MUSS AUCH NOCH ANGEPASST WERDEN 2xint
            sql_statement = """
            
                
                
                SELECT CONVERT(TIME, booking.start) AS start_time, CONVERT(TIME, booking.[end]) AS end_time, pause
                FROM booking
                WHERE fk_position = %s 
                AND CAST(booking.start AS DATE) = CONVERT(date, %s, 104);
                
        
            """
            cursor.execute(sql_statement, [id, currentDay])
            # Fetch the results
            result = [{"start_time_booking": row[0], "end_time_booking": row[1], "pause_booking": row[2]}
                      for row in cursor.fetchall()]

        # Process 'result' and return JsonResponse
        return JsonResponse({"bookingTimes": result})
