from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from documents.models import advanceFcompany
from .serializers import advanceFcompanySerializer
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


class AdvancedFcompanyView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,GenericAPIView):
    queryset = advanceFcompany.objects.all()
    serializer_class = advanceFcompanySerializer
    pagination_class = PageNumberPagination
      
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
