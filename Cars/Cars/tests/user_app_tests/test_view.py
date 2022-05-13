from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from Cars.cars_rest.models import CarBrand
from Cars.users_app.models import CustomCarUser






class RegistrationPageTest(TestCase):
    UserModel=get_user_model()
    test_username="ani"
    test_password='1234'
    def test_success_stored_new_user_in_Db(self):
        user_data = {
            "username": self.test_username,
            'password': self.test_password
        }
        self.UserModel.objects.create_user(**user_data)
        self.client.login()
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

class CreateNewBrandTest(TestCase):
    UserModel = get_user_model()
    test_username = "ani"
    test_password = '1234'
    test_carbrand='AUDI'

    def __log_user(self):
        """ for login the user"""
        user_data = {
            "username": self.test_username,
            'password': self.test_password
        }
        self.UserModel.objects.create_user(**user_data)
        self.client.login()

    def test_create_new_brand(self):
        #self.__log_user()
        new_brand=CarBrand(name=self.test_carbrand)
        new_brand.save()
        last_created_brand=CarBrand.objects.last()
        self.assertEqual(self.test_carbrand,last_created_brand.name)
        self.assertEqual(None,last_created_brand.deleted_at)


    def test_update_brand(self):
        new_name='BMW'
        new_brand = CarBrand(name=self.test_carbrand)
        new_brand.save()
        brand_for_update = CarBrand.objects.last()
        brand_for_update.name=new_name
        brand_for_update.save()
        self.assertEqual(new_name,brand_for_update.name)

    def test_new_brand__to_long___return_error(self):
        new_name = 'BMWvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
        new_brand = CarBrand(name=new_name)
        with self.assertRaises(Exception) as context:
            new_brand.full_clean()
            new_brand.save()
        self.assertIsNotNone(context.exception)
        # new_brand.save()
        # self.assertRaises(ValidationError)
        #self.assertIsNone(context.exception)

        # brand_for_update = CarBrand.objects.last()
        # self.assertEqual(new_brand.name,new_name)
        # brand_for_update.name = new_name
        # # with self.assertRaises(Exception) as context:
        # #     brand_for_update.save()
        # # self.assertIsNone(context.exception)
        #
        #
        # self.assertRaises(ValidationError)
        # self.assertEqual(new_name, brand_for_update.name)



