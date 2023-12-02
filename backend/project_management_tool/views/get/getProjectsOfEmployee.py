from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ...models import Positon, Project
from ...middleware import validator
import json
from ...middleware import sqlQuery 
@csrf_exempt

parameter_value = 123  # Hier setzt du den gewünschten Wert für den Parameter ein
project_instance = ProjectsFromEmployee(parameter_value)
result = project_instance.toJsonTotal()

# Hier kannst du mit dem Ergebnis arbeiten
print(result)
