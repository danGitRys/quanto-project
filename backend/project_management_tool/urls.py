from django.urls import path

from backend.project_management_tool.views.get import getProjectsForEmployee
from .views import *
from .views.time.getTime import getTime

urlpatterns = [
    path('', viewstemp.hello_world, name="home"),
    path('login/', viewstemp.loginpage),
    path('api/', viewstemp.api),
    path('test', positionView.view_a),
    path('getEmployee', employee.getEmployee),
    path('login', login),

    path('team',createTeam,name="createTeam"),
    path('createAssignment',createAssignment, name='createAssignment'),
    

    
    path('employee', createEmployee),
    path('booking', createBooking),
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
    path('getEmployeesToProjectId/<int:id>', getEmployeesToProjectId),
    path('getProjectsForEmployee/<int:id>', getProjectsForEmployee)



]
