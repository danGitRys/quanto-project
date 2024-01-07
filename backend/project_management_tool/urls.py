from django.urls import path

from .views.get.allTeams import getAllTeams
from .views.get.teamroles import getTeamRoles
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
    path('team/get/all',getAllTeams),
    path('team/get/roles',getTeamRoles),
    path('employee/new',createEmployee),
    
    #New Project Routes
    path('employee/get/all', getAllEmployees),
    path('project/new',createProject),

    path('login',login),

    path('assignment/new',createAssignment, name='createAssignment'),
    path('team/new',createTeam),
    path('position/new',createPositon, name='createPosition'),

    # ?
    path('employee/get/role',getRole, name='getRole'),
    path('assignedProjects/<int:id>', getAssignedProjects),
    
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
    path('assignment/<int:assignment_id>/delete', deleteAssignment),
    path('booking/<int:id>/delete', deleteBooking),
    path('employee/<int:id>/delete', deleteEmployee),
    path('forecast/<int:id>/delete', deleteForecast),
    path('project/<int:id>/delete', deleteProject),
    path('team/<int:id>/delete', deleteTeam),
    path('assignment/<int:assignment_id>/update', updateAssignment),
    path('team/get/<int:id>', getTeam),
    path('project/get/<int:id>', getProject),
    path('position/get/<int:id>', getPosition),
    path('forecast/get/<int:id>', getForecast),
    path('employee/get/<int:id>', getEmployee),
    path('booking/get/<int:id>', getBooking),
    path('assignment/get/<int:id>', getAssignment),
    path('getPositionsToProjectId/<int:id>', getPositionsToProjectId),
    path('getEmployeesToProjectId/<int:id>', getEmployeesToProjectId),
    path('getProjectsOfEmployee/<int:id>', getProjectsOfEmployee),
    path('getProjectsForEmployee/<int:id>', getProjectsForEmployee),

 
    path('getTest/<int:id>/<int:projectKey>',getTest),
    path('getBookingTimes/<int:id>/<str:currentDay>',getBookingTimes),
    path('getProjectsWhereProjectLeader/<int:id>', getProjectsWhereProjectLeader),
    path('getForecastForDay/<int:id>/<str:currentDay>/<int:empId>',getForecastForDay),
    path('getBookingTimesForDay/<int:id>/<str:currentDay>/<int:empId>', getBookingTimesForDay),
    path('updateBooking/<int:booking_id>', updateBooking),
    path('getAllPositionsFromAllProjects/<int:id>', getAllPositionsFromAllProjects),

    path('getPositionsOfProjectOfEmployee/<int:id>/<int:empId>',getPositionsOfProjectOfEmployee),

    path('positionGraph/<id>',PositionGraphView.as_view()),
    path('positionGraph',PositionGraphView.as_view()),
    path('positionLinearGraph/<id>',PositionLinearGraphView.as_view()),
    path('positionLinearGraph',PositionLinearGraphView.as_view()),
    path('projectPositionsLinearGraph/<id>',ProjectPositionsGraphView.as_view()),
    path('projectPositionLinearGraph',ProjectPositionsGraphView.as_view()),
    path('projectPositionsPieGraph/<id>',ProjectPositionsPieGraphView.as_view()),
    path('projectPositionPieGraph',ProjectPositionsPieGraphView.as_view()),
    path('projectProjectionGraph/<int:id>/<int:weeks>',ProjectProjectionGraphView.as_view()),
    path('projectProjectionGraph',ProjectProjectionGraphView.as_view()),
    
    
    path('getTableData/<int:id>',getTableData),
    path('getAllProjects/',getAllProjects),




    path('timeTableBooking/<id>',TimeTableBookingView.as_view()),
    path('timeTableBooking',TimeTableBookingView.as_view()),
    path('timeTableForecast/<id>',TimeTableForecastView.as_view()),
    path('timeTableForecast',TimeTableForecastView.as_view()),
    path('timeTableCombined/<id>',TimeTableCombinedView.as_view()),
    path('timeTableCombined',TimeTableCombinedView.as_view()),

]


