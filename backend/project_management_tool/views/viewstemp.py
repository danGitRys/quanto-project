from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404

from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import *

# Request-handler

# Create your views here.
@csrf_exempt
def hello_world(request):
    print("___")
    print(request.POST)
    post_data = request.body.decode('utf-8')
    print(post_data)
    loggedIn = True
    if not loggedIn:
        loggedIn = False
    x = 1
    y = 2
    with connection.cursor() as cursor:
        #cursor.execute("SELECT volume_ream FROM positions ")
        allObjects = Employee.objects.all()
        for emp in allObjects:
            print(emp.forename)
        print(allObjects)
       # rows = cursor.fetchall()
        #print(rows)
    data = {
        'key1': 'value1',
        'key2': 'value2',
        # Add more key-value pairs as needed
    }
    return JsonResponse(data)

def loginpage(request):
    #bekomme irgendein JSON
    json = json.loads(request)

    #Session-token
    #token = json
    return 

def api(request):
    return HttpResponse("API")



def orm_Test(request):


    currsor = connection.cursor()
    result = currsor.execute('''EXEC getEmployeeCalendar @id=2''')


    for res in result:
        print(res)

    response = {
        "test":1
    }
    return JsonResponse(response)


    ...