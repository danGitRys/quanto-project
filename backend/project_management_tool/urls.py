from django.urls import path
from .views import *
from .views.time.getTime import getTime
from .views.basic.assignment import AssignmentView
from .views.basic.team import TeamView
from django.urls import re_path



urlpatterns = [
    path('', viewstemp.hello_world, name="home"),
    path('login/', viewstemp.loginpage),
    path('api/', viewstemp.api),
   
    #path('getEmployee', employee.getEmployee),
  

    #Add Employee to DB Routes
    path('getTeams',getTeams),
    path('getTeamRoles',getTeamRoles),
    
    #New Project Routes
    path('getAllEmployees', getAllEmployees),
    path('getAllEmployeeNames', getAllEmployeeNames),
    path('createProject',createProject),

    path('login',login),
    path('createAssignment',createAssignment, name='createAssignment'),
    path('createPosition',createPositon, name='createPosition'),
    path('createTeam',createTeam),
    path('createEmployee',createEmployee),
    #path('booking',bookingView),
    #path('createForecast',createForecast),

    path('createProject',createProject),
    path('getTeams',getTeams),
    path('getTeamRoles',getTeamRoles),
    path('test/', MyView.as_view()),
    path('test/<id>',MyView.as_view()),
    path('assignment/<id>',AssignmentView.as_view()),
    path('assignment',AssignmentView.as_view()),
    path('team/<id>',TeamView.as_view()),
    path('team',TeamView.as_view()),
    path('project/<id>',ProjectView.as_view()),
    path('project',ProjectView.as_view()),
    path('forecast/<id>',ForecastView.as_view()),
    path('forecast',ForecastView.as_view()),
    path('employee/<id>',EmployeeView.as_view()),
    path('employee',EmployeeView.as_view()),
    path('booking/<id>',BookingView.as_view()),
    path('booking',BookingView.as_view()),
    path('createSQLbookings',createBookingsSql),
    path('createSQLForecasts',createForecastsSql),
    
    #path('employee', createEmployee),
    #path('createBooking', createBooking),
    #path('forecast', createForecast),
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
    path('getEmployeesToProjectId/<int:id>', getEmployeesToProjectId),
    path('getProjectsOfEmployee/<int:id>', getProjectsOfEmployee),
    path('getPositionsOfProjectOfEmployee/<int:id>',getPositionsOfProjectOfEmployee),
    path('getTest/<int:id>/<int:projectKey>',getTest),
    path('getBookingTimes/<int:id>/<str:currentDay>',getBookingTimes),
    path('getProjectsWhereProjectLeader/<int:id>', getProjectsWhereProjectLeader),
    path('getForecastForDay/<int:id>/<str:currentDay>/<int:empId>',getForecastForDay),
    path('getBookingTimesForDay/<int:id>/<str:currentDay>/<int:empId>', getBookingTimesForDay),
]
