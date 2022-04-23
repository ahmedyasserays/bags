import django_filters

from .models import *



class Company_filter(django_filters.FilterSet):
    class Meta:
        model = advanceFcompany
        fields = '__all__'

class document_filter(django_filters.FilterSet):
    start_date = django_filters.DateFilter('documentDate', 'gte')
    end_date = django_filters.DateFilter('documentDate', 'lte')

    class Meta:
        model = uplaodingDocument
        fields = ('start_date', 'end_date','documentNumber','DocumentType','itemType')
