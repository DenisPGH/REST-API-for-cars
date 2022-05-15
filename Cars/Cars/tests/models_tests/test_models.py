from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from Cars.cars_rest.models import CarBrand, CarModel




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
        self.assertEqual(0, len(CarModel.objects.all()))
        self.assertEqual(carmodel['name'], CarModel.all_objects_in_db.last().name)