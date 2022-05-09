from django.shortcuts import render

from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django_filters import rest_framework as filters_rest
from rest_framework import generics as api_views,permissions

from Cars.users_app.models import CustomCarUser


class InfoAllUsersSerializer(serializers.ModelSerializer):
    """show the date from the db"""
    class Meta:
        model = CustomCarUser
        fields = '__all__'


class MyFilterSet(filters_rest.FilterSet):
    class Meta:
        model = CustomCarUser
        fields = ('id',)




class UsersListView(api_views.ListAPIView):
    """ show all users in the implemented html page"""
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = InfoAllUsersSerializer
    filter_backends = [filters_rest.DjangoFilterBackend]
    filterset_class=MyFilterSet
    def get_queryset(self,**kwargs):
        query=''
        search_id = self.request.query_params.get('id', None)
        queryset=CustomCarUser.objects.all()
        if search_id:
            query=queryset.filter(id=search_id)
        else:
            query=queryset
        return query
