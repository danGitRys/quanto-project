from django.shortcuts import render
from django.http import HttpResponse

# Request-handler

# Create your views here.

def hello_world(request):
    x = 1
    y = 2
    return render(request, 'HelloWorld.html', { 'name' : 'Fabi' })

def loginpage(request):


    return HttpResponse(request, 'LOGINPAGE')