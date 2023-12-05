from django.urls import path
from .views import *

urlpatterns = [
    path('', viewstemp.hello_world, name="home"),
    path('login/', viewstemp.loginpage),
    path('api/', viewstemp.api),
    path('test',positionView.view_a),
    path('getEmployee', employee.getEmployee),
    path('login',login),
    
    path('createTeam',createTeam),
    path('createAssignment',createAssignment),
    path('createEmployee',createEmployee),
    path('createBooking',createBooking),
    path('createForecast',createForecast),
    path('createProject',createProject),
    path('getTeams',getTeams),
    path('getTeamRoles',getTeamRoles),
    

    
  
]