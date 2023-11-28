from ..middleware.validation.dateValidator import dateValidator
from ..models import *
from django.test import TestCase
from django.urls import reverse
import json
class PostTestClass(TestCase):

    def test_teamPost(self):
        url = reverse('createTeam')  # Assuming the URL pattern name is 'my_view'
        data = {
                "name":"test5",
                "info":"test2"
                }
        response = self.client.post(url, data, content_type='application/json')
        teamExists:bool = Team.objects.filter(name="test5").exists()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(teamExists,True)

    def test_teamPostFail(self):
        url = reverse('createTeam')  # Assuming the URL pattern name is 'my_view'
        data = {
                "name":"test5",
                "info":"test2"
                }
        response = self.client.get(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        request_data = json.loads(response.content)
        successStatus = request_data["success"]
        self.assertEqual(successStatus, False)
    
    def test_assignmentPost(self):
         url = reverse('createAssignment')  # Assuming the URL pattern name is 'my_view'
         data = {
                "name":"test5",
                "info":"test2"
                }
         response = self.client.get(url, data, content_type='application/json')
         self.assertEqual(response.status_code, 200)
         request_data = json.loads(response.content)
         successStatus = request_data["success"]
         self.assertEqual(successStatus, False)
       
    
    


#Run Comand
#python manage.py test --settings=quantoserver.settings.baseTest