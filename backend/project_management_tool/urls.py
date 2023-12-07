from django.urls import path
from .views import *
from .views.time.getTime import getTime
from .views.basic.assignment import AssignmentView
from django.urls import re_path



urlpatterns = [
    path('', viewstemp.hello_world, name="home"),
    path('login/', viewstemp.loginpage),
    path('api/', viewstemp.api),
   
    path('getEmployee', employee.getEmployee),
  

    path('login',login),
    path('createAssignment',createAssignment, name='createAssignment'),
    path('createPosition',createPositon, name='createPosition'),
    path('createTeam',createTeam),
    path('createEmployee',createEmployee),
    #path('booking',bookingView),
    path('createForecast',createForecast),
    path('createProject',createProject),
    path('getTeams',getTeams),
    path('getTeamRoles',getTeamRoles),
    path('test/', MyView.as_view()),
    path('test/<id>',MyView.as_view()),
    path('assignment/<id>',AssignmentView.as_view()),
    path('assignment',AssignmentView.as_view()),
    

    
    path('employee', createEmployee),
    #path('createBooking', createBooking),
    path('forecast', createForecast),
    path('project', createProject),
    path('currentTime',getTime),
    path('deleteAssignment/<int:assignment_id>', deleteAssignment),
    path('deleteBooking/<int:id>', deleteBooking),
    path('deleteEmployee/<int:id>', deleteEmployee),
    path('deleteForecast/<int:id>', deleteForecast),
    path('deleteProject/<int:id>', deleteProject),
    path('deleteTeam/<int:id>', deleteTeam),
    path('updateAssignment/<int:assignment_id>', updateAssignment),
    path('getTeam/<int:id>', getTeam),
    path('getProject/<int:id>', getProject),
    path('getPosition/<int:id>', getPosition),
    path('getForecast/<int:id>', getForecast),
    path('getEmployee/<int:id>', getEmployee),
    path('getBooking/<int:id>', getBooking),
    path('getAssignment/<int:id>', getAssignment),
    path('assignedProjects/<int:id>', getAssignedProjects),
    path('getPositionsToProjectId/<int:id>', getPositionsToProjectId),
    path('getEmployeesToProjectId/<int:id>', getEmployeesToProjectId)



]
