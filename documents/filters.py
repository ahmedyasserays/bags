import django_filters

from .models import *



class Company_filter(django_filters.FilterSet):
    class Meta:
        model = advanceFcompany
        fields = '__all__'