from django.test import TestCase, Client
from django.urls import reverse
from .models import Runtracker
from .views import index, newForm, addRun
from .forms import RuntrackerForm


# Create your tests here.
class ModelTest(TestCase):
    def test_fields(self):
        item = Runtracker()
        item.date = "2019-10-29"
        item.distance = 3000
        item.time = 90
        item.calories = 0
        item.save()

        record = Runtracker.objects.get(pk=1)

        self.assertEqual(record, item)

class ViewsTest(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runtracker/index.html')

    def test_newForm(self):
        client = Client()
        response = client.get(reverse('formm'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'runtracker/form.html')

    def test_addRun(self):
        client = Client()
        post_data = {
            'date' :"2019-10-29",
            'distance' : 3000,
            'time' : 90,
            'calories' : 0
        }
        response = client.post(reverse('add'), post_data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')

class FormTests(TestCase):
    def test_form_false(self):
        form_data = {'something': 'something'}
        form = RuntrackerForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_true(self):
        form_data = {
            'date' :"2019-10-29",
            'distance' : 3000,
            'time' : 90,
            'calories' : 0
        }
        form = RuntrackerForm(data=form_data)

        self.assertTrue(form.is_valid())