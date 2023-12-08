from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
@method_decorator(csrf_exempt, name='dispatch')

class MyView(View):
    def get(self, *args, **kwargs):
        id_param = kwargs.get('id')
        print(id_param)
        return HttpResponse("Get")

    def post(self,request, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)
        print(request.body)
        request_data = json.loads(request.body)
        print(request_data)
        return HttpResponse('Post')
    def put(self, *args, **kwargs):
        return HttpResponse('Put')
    
    def delete(self, *args, **kwargs):
        return HttpResponse('delete')