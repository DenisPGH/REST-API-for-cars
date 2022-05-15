from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.users_app.models import CustomCarUser


class UserCartests(TestCase):
    UserModel = get_user_model()
    test_carbrand = {'name': "Audi", }

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.client = None

    def __create_arrange_for_car(self):

        test_brand = CarBrand(name=self.test_carbrand['name'])
        test_brand.save()
        carmodel = {
            'name': "TT",
            'car_brand': CarBrand.objects.get(name=self.test_carbrand['name'])
        }
        new_model = CarModel(**carmodel)
        new_model.save()
        test_user = {
            "username": "Gosho",
            'password': "123"
        }
        self.UserModel.objects.create_user(**test_user)
        self.client.login(**test_user)




    def test_creation_new_car__valid_data___return_sucess(self):
        self.__create_arrange_for_car()
        new_car={
              "user": 1,
              "car_brand": 1,
              "car_model": 1,
              "first_reg": "2022-05-15",
              "odometer": 1000
            }

        response = self.client.post(
            reverse('cars',kwargs=None), new_car, content_type='application/json')
        # print(response.json())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, len(UserCar.all_objects_in_db.all()))
        self.assertEqual(CarBrand.objects.last().name, UserCar.objects.last().car_brand.name)


    def test_creation_new_car__invalid_data___return_error_message(self):
        self.__create_arrange_for_car()
        new_car={
              "user": 'a',
              "car_brand": 1,
              "car_model": 1,
              "first_reg": "2022-05-15",
              "odometer": 1000
            }

        response = self.client.post(
                reverse('cars',kwargs=None), new_car, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_update_a_car__valid_data(self):
        self.__create_arrange_for_car()
        new_car = {
            "user": 1,
            "car_brand": 1,
            "car_model": 1,
            "first_reg": "2022-05-15",
            "odometer": 1000
        }
        response = self.client.post(
            reverse('cars', kwargs=None), new_car, content_type='application/json')
        updated_car={
            "user": 1,
            "car_brand": 1,
            "car_model": 1,
            "first_reg": "2022-05-15",
            "odometer": 1000000
        }
        car_for_update=UserCar.objects.last()
        response = self.client.put(
            reverse('single car', kwargs={'pk':car_for_update.pk}), updated_car, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_car['odometer'], response.json()['odometer'])

    def test_update_a_car__invalid_data__return_error_message(self):
        self.__create_arrange_for_car()
        new_car = {
            "user": 1,
            "car_brand": 1,
            "car_model": 1,
            "first_reg": "2022-05-15",
            "odometer": 1000
        }
        response = self.client.post(
            reverse('cars', kwargs=None), new_car, content_type='application/json')
        updated_car={
            "user": "a",
            "car_brand": 'a',
            "car_model": 'b',
            "first_reg": "2022-05",
            "odometer": "a"
        }
        car_for_update=UserCar.objects.last()
        response = self.client.put(
            reverse('single car', kwargs={'pk':car_for_update.pk}), updated_car, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        error_message_user=''.join(response.json()['user'])
        error_message_carbrand=''.join(response.json()['car_brand'])
        error_message_carmodel=''.join(response.json()['car_model'])
        error_message_odometer=''.join(response.json()['odometer'])
        error_message_first_reg=''.join(response.json()['first_reg'])

        self.assertIn('Incorrect type',error_message_user)
        self.assertIn('Incorrect type',error_message_carbrand)
        self.assertIn('Incorrect type',error_message_carmodel)
        self.assertIn('A valid integer is required.',error_message_odometer)
        self.assertIn('Date has wrong format',error_message_first_reg)



    def test_soft_delete_a_car__deleted_at(self):
        self.__create_arrange_for_car()
        new_car = {
            "user": CustomCarUser.objects.last(),
            "car_brand": CarBrand.objects.last(),
            "car_model": CarModel.objects.last(),
            "first_reg": "2022-05-15",
            "odometer": 1000
        }
        new=UserCar(**new_car)
        new.save()
        car_for_delete = UserCar.objects.last()
        response = self.client.delete(
            reverse('single car', kwargs={'pk': f"{car_for_delete.pk}"}),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(UserCar.all_objects_in_db.all()))
        self.assertEqual(0, len(UserCar.objects.all()))
        self.assertEqual(new_car['odometer'], UserCar.all_objects_in_db.last().odometer)