
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework as filters_rest
from rest_framework import generics as api_views,permissions
from Cars.cars_rest.models import CarBrand, CarModel, UserCar
from Cars.cars_rest.serializers import InfoAllUsersSerializer, CarBrandSerializer, CarModelSerializer, \
    CreateCarSerializer, CarSerializer, CarBrandListSerializer, UpdateUsersSerializer, \
    UpdateCarSerializer, UpdateCarModelSerializer
from Cars.users_app.models import CustomCarUser



""" ==============here USER logic==============================="""
class UserFilterSet(filters_rest.FilterSet):
    """you can filter the users, by iD or hometown"""
    class Meta:
        model = CustomCarUser
        fields = ('id','hometown')

class UserViewSet(viewsets.ModelViewSet):
    """ show details,update,delete for one user"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset = CustomCarUser.objects.all()
    serializer_class = UpdateUsersSerializer

    def show(self, request,pk=None, *args, **kwargs):
        user = CustomCarUser.objects.get(pk=pk)
        if not user.deleted_at:
            serializer = UpdateUsersSerializer(user)
            return Response(serializer.data)
        else:
            return Response({f"Username: {user.username}": f"was deleted at {user.deleted_at}"})


    def put(self, request, pk=None):
        user = CustomCarUser.objects.get(pk=pk)
        data = request.data
        serializer = UpdateUsersSerializer(data=request.data)
        if serializer.is_valid() and user.deleted_at==None: # could update only active users
            user.first_name=data['first_name']
            user.last_name=data['last_name']
            user.hometown=data['hometown']
            user.data_birth=data['data_birth']
            user.picture=data['picture']
            user.save()
            serializer_2 = UpdateUsersSerializer(user)
            return Response(serializer_2.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request,pk=None, *args, **kwargs):
        user = CustomCarUser.objects.get(pk=pk)
        user.delete()
        return Response({f"{user.username}":'deleted'})




class UsersListView(api_views.ListAPIView):
    """ show all users in the implemented html page"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    serializer_class = InfoAllUsersSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class=UserFilterSet
    queryset = CustomCarUser.objects.all()





"""===== here are the BRAND logic================================"""
class BrandsViewSet(viewsets.ModelViewSet):
    """show all brands names and create new brand"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandListSerializer


class SingleBrandViewSet(viewsets.ModelViewSet):
    """show details for one brand, update, delete"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

    def show(self, request, pk=None, *args, **kwargs):
        brand = CarBrand.objects.get(pk=pk)
        if not brand.deleted_at:
            serializer = CarBrandSerializer(brand)
            return Response(serializer.data)
        else:
            return Response({f"Brand with name: {brand.name}": f"deleted at {brand.deleted_at}"})

    def put(self, request, pk=None):
        brand = CarBrand.objects.get(pk=pk)
        data = request.data
        serializer=CarBrandSerializer(data=request.data)
        if serializer.is_valid():
            brand.name = data['name']
            brand.save()
            serializer_2 = CarBrandSerializer(brand)
            return Response(serializer_2.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        brand=CarBrand.objects.get(pk=pk)
        brand.delete()
        return Response({f"{brand.name}": 'deleted'})






"""=================== here are the MODELCAR logic==========================="""


class ListModels(api_views.ListCreateAPIView):
    """ show all models, can create new model"""
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class SingleCarModelView(api_views.RetrieveUpdateDestroyAPIView):
    """ singe model details, update and delete"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset = CarModel.objects.all()
    serializer_class = UpdateCarModelSerializer





"""=================== here are the CAR logic============================"""

class CarsFilterSet(filters_rest.FilterSet):
    class Meta:
        model = UserCar
        #fields = ('user','car_brand','car_model','first_reg','odometer')
        fields={
            'first_reg':['gt','lt'],
            'user':['exact'],
            'car_brand':['exact'],
            'car_model':['exact'],
            'odometer':['gt','lt'],

        }


class SingleCarViewSet(viewsets.ModelViewSet):
    """show details, update and delete each single car object"""
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.BasePermission
    )
    queryset =  UserCar.objects.all()
    serializer_class = CarSerializer
    def show(self, request,pk=None, *args, **kwargs):
        car = UserCar.objects.get(pk=pk)
        if not car.deleted_at:
            serializer = UpdateCarSerializer(car)
            return Response(serializer.data)
        else:
            return Response({f"Car: {car.car_model}": f"was deleted at {car.deleted_at}"})


    def put(self, request, pk=None):
        car = UserCar.objects.get(pk=pk)
        data = request.data
        serializer = UpdateCarSerializer(data=request.data)
        if serializer.is_valid():
            car.car_model = CarModel.objects.get(id=data['car_model'])
            car.car_brand = CarBrand.objects.get(id=data['car_brand'])
            car.first_reg = data['first_reg']
            car.odometer = data['odometer']
            car.save()
            serializer_2 = UpdateCarSerializer(car)
            return Response(serializer_2.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request,pk=None, *args, **kwargs):
        car = UserCar.objects.get(pk=pk)
        car.delete()
        return Response({f"{car.car_model}":'deleted'})



class ListCars(api_views.ListCreateAPIView):
    """ show all cars, can create new one"""
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = UserCar.objects.all()
    serializer_class = CreateCarSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class = CarsFilterSet









