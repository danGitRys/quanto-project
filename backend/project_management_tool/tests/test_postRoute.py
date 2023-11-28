from ..middleware.validation.dateValidator import dateValidator
from ..models import *
from django.test import TestCase
from django.urls import reverse
class PostTestClass(TestCase):

    def test_First(self):
        url = reverse('createTeam')  # Assuming the URL pattern name is 'my_view'
        data = {
                "name":"test5",
                "info":"test2"
                }
        response = self.client.post(url, data, content_type='application/json')
        teamExists:bool = Team.objects.filter(name="test5").exists()
        print(teamExists)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

#Run Comand
#python manage.py test --settings=quantoserver.settings.baseTest