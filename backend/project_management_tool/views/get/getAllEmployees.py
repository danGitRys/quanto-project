from django.http import JsonResponse
from ...models import Employee


def getAllEmployees(request):
    employees = []
    employeeNames = []
    allEmployees = Employee.objects.all()
    for emp in allEmployees:
        employees.append(emp.toJson())
        employeeNames.append(emp.forename + " " + emp.surname)
    if request.method == 'GET':
        response_data = { 
            "employees": employees,
            "employeeNames": employeeNames,
        }
    return JsonResponse(response_data)

def getAllEmployeeNames(request):
    employeeIDs = []
    employeeNames = []
    allEmployees = Employee.objects.all()
    for emp in allEmployees:
        employeeIDs.append(emp.emp_id)
        employeeNames.append(emp.forename + " " + emp.surname)
    if request.method == 'GET':
        response_data = { 
            "employeeNames": employeeNames,
        }
    return JsonResponse(response_data)