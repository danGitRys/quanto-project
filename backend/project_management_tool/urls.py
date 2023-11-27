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
    path('createAssignment',createAssignment),
    path('employee',createEmployee),
    path('booking',createBooking),
    path('forecast',createForecast),
    path('project',createProject),
    path('deleteAssignment/<int:assignment_id>',deleteAssignment),
    path('deleteBooking/<int:id>',deleteBooking)
    

    
  
]