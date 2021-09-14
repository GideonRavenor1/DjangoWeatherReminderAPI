import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from City.models import CityApp
from Sublist.models import SubListApp
from User.models import UserApp
from Weather.models import WeatherApp

list_urls = {
    'City:add_city',
    'City:all_cities',
    'Sublist:add_subscription',
    'Sublist:addAdmin_subscription',
    'Sublist:sublistapp-list',
    'User:createAdmin_user',
    'User:userapp-list'}

list_pk_urls = [
    'City:detail_city',
    'Sublist:user_subscription',
    'Sublist:delete_subscription',
    'Sublist:deleteAdmin_subscription',
    'Sublist:sublistapp-detail',
    'User:delete_user',
    'User:update_user',
    'User:delete_updateAdmin_user',
    'User:userapp-detail',
]


class CityAndWeatherTests(APITestCase):

    def setUp(self):
        self.user = UserApp.objects.create(username='john', password='johnpassword',
                                           email='lennon@thebeatles.com', is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_post_delete_city(self):
        url = reverse('City:add_city')
        data = {'name': 'Moscow'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CityApp.objects.count(), 1)
        self.assertEqual(CityApp.objects.get().name, 'Moscow')

        self.assertEqual(WeatherApp.objects.count(), 1)
        self.assertEqual(WeatherApp.objects.get().city.name, 'Moscow')

        url = reverse('City:detail_city', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CityApp.objects.count(), 0)

        self.assertEqual(WeatherApp.objects.count(), 0)

    def test_list_cities(self):
        url = reverse('City:add_city')
        data1 = {'name': 'New York'}
        data2 = {'name': 'Chicago'}
        response1 = self.client.post(url, data1, format='json')
        response2 = self.client.post(url, data2, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CityApp.objects.count(), 2)

        url = reverse('City:all_cities')
        response3 = self.client.get(url)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)


class PermissionsTests(APITestCase):

    def setUp(self):
        self.user = UserApp.objects.create(username='test', password='johnpassword',
                                           email='lennon@thebeatles.com')
        self.client = APIClient()

    def test_permissions_not_authorized_user(self):

        for url in list_urls:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        for url in list_pk_urls:
            response = self.client.get(reverse(url, args=[str(random.randint(1, 100))]))
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permissions_not_admin_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('Sublist:addAdmin_subscription')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('User:createAdmin_user')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('Sublist:deleteAdmin_subscription', args=[str(random.randint(1, 100))])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('User:delete_updateAdmin_user', args=[str(random.randint(1, 100))])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserTests(APITestCase):

    def setUp(self):
        self.user1 = UserApp.objects.create(username='john', password='johnpassword',
                                            email='lennon@thebeatles.com', is_staff=True)
        self.user2 = UserApp.objects.create(username='Marina', password='ytrewq199325',
                                            email='qwerty@email.com')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_user_create_delete_update(self):
        url = reverse('User:createAdmin_user')
        data = {
            'username': 'Nika',
            'password': 'ytrewq199325',
            'email': 'test@email.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserApp.objects.count(), 3)
        self.assertEqual(UserApp.objects.get(username='Nika').username, 'Nika')

        url = reverse('User:delete_updateAdmin_user', args=[self.user2.pk])
        data = {
            'username': 'Marinka',
            'password': 'ytrewq199325',
            'email': 'test@email.com'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserApp.objects.get(username='Marinka').username, 'Marinka')
        data = {
            'username': 'Marink',
            'password': 'ytrewq199325qqq',
            'email': 'test123@email.com'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserApp.objects.get(username='Marink').username, 'Marink')

        url = reverse('User:update_user', args=[self.user1.pk])
        data = {
            'username': 'Fedor',
            'password': 'johnpassword',
            'email': 'lennon@thebeatles.com'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserApp.objects.get(username='Fedor').username, 'Fedor')
        data = {
            'username': 'Fred',
            'password': 'ytrewq199325',
            'email': 'test123@email.com'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserApp.objects.get(username='Fred').username, 'Fred')

        url = reverse('User:delete_updateAdmin_user', args=[self.user2.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserApp.objects.count(), 2)

        url = reverse('User:delete_user', args=[self.user1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserApp.objects.count(), 1)

    def test_get_users(self):
        url = reverse('User:userapp-detail', args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('User:delete_user', args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('User:update_user', args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('User:delete_updateAdmin_user', args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SublistTest(APITestCase):

    def setUp(self):
        self.user1 = UserApp.objects.create(username='john', password='johnpassword',
                                            email='lennon@thebeatles.com', is_staff=True)
        self.user2 = UserApp.objects.create(username='Marina', password='ytrewq199325',
                                            email='qwerty@email.com')
        self.city = CityApp.objects.create(name='Moscow')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_sublist_get_create_delete_update(self):
        url = reverse('Sublist:add_subscription')
        data = {
            'user_id': self.user1.pk,
            'city_id': self.city.pk,
            'send_email': 6
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubListApp.objects.count(), 1)
        self.assertEqual({'city_id': self.city.pk, 'name': self.city.name, 'send_email': 6},  response.data)

        url = reverse('Sublist:addAdmin_subscription')
        data = {
            'user_id': self.user2.pk,
            'city_id': self.city.pk,
            'send_email': 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubListApp.objects.count(), 2)
        self.assertEqual({'user_id': self.user2.pk, 'city_id': self.city.pk, 'send_email': 3,
                          'username': self.user2.username, 'city': self.city.name}, response.data)

        url = reverse('Sublist:sublistapp-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('Sublist:sublistapp-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('Sublist:delete_subscription', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SubListApp.objects.count(), 1)

        url = reverse('Sublist:deleteAdmin_subscription', args=[2])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SubListApp.objects.count(), 0)










