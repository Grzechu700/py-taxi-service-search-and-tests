from django.test import TestCase, Client
from django.urls import reverse
from .models import Driver

class DriverSearchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.driver1 = Driver.objects.create(username='driver1')
        self.driver2 = Driver.objects.create(username='driver2')

    def test_search_by_username(self):
        response = self.client.get(reverse('driver_list'), {'q': 'driver1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'driver1')
        self.assertNotContains(response, 'driver2')

    def test_no_search_query(self):
        response = self.client.get(reverse('driver_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'driver1')
        self.assertContains(response, 'driver2')
