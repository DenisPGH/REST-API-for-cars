from django.test import TestCase
from django.contrib.auth import get_user_model
from Cars.cars_rest.models import CarBrand


class BrandsTests(TestCase):
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
        self.client.login(**user_data)

    def test_create_new_brand__valid_data(self):
        self.__log_user()
        new_brand=CarBrand(name=self.test_carbrand)
        new_brand.save()
        last_created_brand=CarBrand.objects.last()
        self.assertEqual(self.test_carbrand,last_created_brand.name)
        self.assertEqual(None,last_created_brand.deleted_at)


    def test_update_brand__valid_data(self):
        new_name='BMW'
        new_brand = CarBrand(name=self.test_carbrand)
        new_brand.save()
        brand_for_update = CarBrand.objects.last()
        brand_for_update.name=new_name
        brand_for_update.save()
        self.assertEqual(new_name,brand_for_update.name)
        self.assertIsNone(brand_for_update.deleted_at)

    def test_new_brand__invalid_name___return_error(self):
        new_name = 'BMWvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv' \
                   'vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'
        new_brand = CarBrand(name=new_name)
        with self.assertRaises(Exception) as context:
            new_brand.full_clean()
            new_brand.save()
        self.assertIsNotNone(context.exception)

    def test_soft_delete_a_brand(self):
        new_name = 'audi'
        new_brand = CarBrand(name=self.test_carbrand)
        new_brand.save()
        brand_for_delete = CarBrand.objects.last()
        brand_for_delete.name = new_name
        brand_for_delete.delete()
        self.assertEqual(new_name, brand_for_delete.name)
        self.assertIsNotNone(brand_for_delete.deleted_at)