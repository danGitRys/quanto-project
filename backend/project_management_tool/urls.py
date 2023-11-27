from django.urls import path
from .views import *

urlpatterns = [
    path('', viewstemp.hello_world, name="home"),
    path('login/', viewstemp.loginpage),
    path('api/', viewstemp.api),
    path('test',positionView.view_a),
    path('getEmployee', employee.getEmployee),
    path('login',login),
    

    path('team',createTeam),
    path('team',createAssignment),
    path('team',createEmployee),
    path('team',createBooking),
    path('team',createForecast),
    path('team',createProject),
    

    
  
]