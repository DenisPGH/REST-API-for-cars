from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from Cars_root.users_app.models import CustomCarUser






class RegistrationPageTests(TestCase):
    UserModel=get_user_model()
    test_username="ani"
    test_password='1234'
    def test_valid_data___success_stored_new_user_in_Db(self):
        user_data = {
            "username": self.test_username,
            'password': self.test_password
        }
        self.UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('loginJ'))
        self.assertTemplateUsed(response, 'index.html')
        registered_user=self.UserModel.objects.last()
        self.assertEqual(self.test_username,registered_user.username)
        self.assertIsNotNone(registered_user.password)
        self.assertEqual('',registered_user.first_name)

    def test_success_registration(self):
        new_profil_data = {
                            'password':'12345',
                            'username':'deni@abv.bg',
                            'first_name': 'deni',
                           'last_name': 'New_name',
                            }
        self.UserModel.objects.create_user(**new_profil_data)
        response=self.client.post(reverse('loginJ'),data=new_profil_data)
        user=CustomCarUser.objects.first()
        self.assertEqual(1,len(CustomCarUser.objects.all()))
        self.assertEqual(new_profil_data['first_name'],user.first_name)



class TestsMainPage(TestCase):
    UserModel = get_user_model()
    test_user = {
        "username": "miro",
        'password': "12345"
    }


    def test_main_page__return_context_data(self):
        self.UserModel.objects.create_user(**self.test_user)
        has=self.client.login(**self.test_user)
        self.assertEqual(True, has)
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'login.html')

        self.assertEqual(1, len(response.context['users']))
        self.assertEqual(0, len(response.context['cars']))
        self.assertEqual(0, len(response.context['models']))
        self.assertEqual(0, len(response.context['brands']))




















