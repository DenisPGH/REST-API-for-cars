from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from Cars.cars_rest.models import CarBrand, CarModel
from Cars.users_app.models import CustomCarUser






class RegistrationPageTest(TestCase):
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



class TestMainPage(TestCase):
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



class BrandsTest(TestCase):
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



class CarModelsTests(TestCase):
    UserModel = get_user_model()
    test_user = {
        "username": "miro",
        'password': "12345"
    }

    def __login_user(self):
        self.UserModel.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)

    def test_valid_data__create_new_model(self):
        test_brand = CarBrand(name='Audi')
        test_brand.save()
        carmodel = {
            'name': "TT",
            'car_brand': CarBrand.objects.get(name='Audi')
        }
        new_model = CarModel(**carmodel)
        new_model.save()
        self.__login_user()
        response = self.client.get(
            reverse('models'), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual(carmodel['name'], response.json()['results'][0]['name'])


    def test_invalid_data__return_exception(self):
        test_brand = CarBrand(name='Audi')
        test_brand.save()
        invalid_carmodel = {
            'name': "TT",
            'car_brand': 1
        }
        with self.assertRaises(Exception) as ex:
            new_model = CarModel(**invalid_carmodel)
            new_model.save()
        self.assertIsNotNone(ex.exception)






    def test_update_a_carmodel__valid_data___return_succes(self):
        test_brand = CarBrand(name='Audi')
        test_brand.save()
        start_carmodel = {
            'name': "TT",
            'car_brand': CarBrand.objects.get(name='Audi')
        }
        new_carmodel = {
            "name": "DENI",
            'car_brand': 1

        }

        new_model=CarModel(**start_carmodel)
        new_model.save()
        self.__login_user()
        for_update=CarModel.objects.last()
        self.assertEqual(1,for_update.pk)
        self.assertEqual(start_carmodel['name'],for_update.name)
        response = self.client.put(
            reverse('single model',kwargs={'pk':for_update.pk}),new_carmodel,content_type='application/json')

        self.assertEqual(response.status_code, 200)
        last_updated_model=CarModel.objects.last()
        last_updated_model.refresh_from_db()
        self.assertEqual(new_carmodel['name'], last_updated_model.name)



    def test_update_a_carmodel__invalid_name___return_error(self):
        test_brand = CarBrand(name='Audi')
        test_brand.save()
        start_carmodel = {
            'name': "TT",
            'car_brand': CarBrand.objects.get(name='Audi')
        }
        new_carmodel = {
            "name": "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
            'car_brand': 1

        }

        new_model=CarModel(**start_carmodel)
        new_model.save()
        self.__login_user()
        for_update=CarModel.objects.last()
        self.assertEqual(1,for_update.pk)
        self.assertEqual(start_carmodel['name'],for_update.name)
        response = self.client.put(
            reverse('single model',kwargs={'pk':for_update.pk}),new_carmodel,content_type='application/json')

        self.assertEqual(response.status_code, 400) # more than 30 char


    def test_soft_delete_a_carmodel(self):
        test_brand = CarBrand(name='Audi')
        test_brand.save()
        carmodel = {
            'name': "Fiat",
            'car_brand': CarBrand.objects.get(name='Audi')
        }

        new_carmodel = CarModel(**carmodel)
        new_carmodel.save()
        model_for_delete = CarModel.objects.last()
        # model_for_delete.delete() # other test for delete
        # self.assertIsNotNone(model_for_delete.deleted_at)
        self.__login_user()
        response = self.client.delete(
            reverse('single model', kwargs={'pk': f"{model_for_delete.pk}"}),content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(1, len(CarModel.all_objects_in_db.all()))
        self.assertEqual(carmodel['name'], CarModel.all_objects_in_db.last().name)







