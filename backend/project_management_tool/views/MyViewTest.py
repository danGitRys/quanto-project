from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')

class MyView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Get")

    def post(self, *args, **kwargs):
        return HttpResponse('Post')