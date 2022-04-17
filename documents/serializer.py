from rest_framework import serializers
from .models import advanceFcompany, uplaodingDocument

class advanceFcompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = advanceFcompany
    fields = ['date', 'idComapny','name','recevingNumber','receivingAmount','expenceNumber','expenceAmount','depositeAmount','paymentAmount','DepPayDate','FCompany','RecLink','NetAmount','receiDepPay','details','notes']
    
    

class uploadingDocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = uplaodingDocument
    fields = ['documentNumber', 'DocumentType','itemType','documentDate','documentFile']


class newFCompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = advanceFcompany
    fields = ['date', 'FCompany','depositeAmount','paymentAmount','DepPayDate', 'NetAmount']