from argparse import ONE_OR_MORE
from email.policy import default
import numbers
from operator import mod
from xml.dom.minidom import DocumentType
from django.db import models
from django.contrib.auth.models import User
from admins.models import f_company,new_document,new_item
import documents
from datetime import datetime

# Create your models here.
class uplaodingDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    documentNumber = models.IntegerField(null=True, default=0)
    DocumentType = models.ForeignKey(new_document,on_delete=models.CASCADE)
    itemType = models.ForeignKey(new_item,on_delete=models.CASCADE)
    documentDate = models.DateField(default=datetime.today)
    file= models.FileField(upload_to="static/")
    
    def __str__(self):
        return str(self.documentNumber)
    
class advanceFcompany(models.Model):
    #Fcompany
    date = models.DateField()
    FCompany =models.ForeignKey(f_company,on_delete=models.CASCADE)
    depositeAmount = models.IntegerField()
    paymentAmount = models.IntegerField()
    DepPayDate = models.DateField()
    NetAmount = models.IntegerField()
    details = models.TextField()
    #advanced Fcompany
    idComapny = models.IntegerField(null=True, default=0,blank=True)
    name =models.CharField(max_length=200,null=True,blank=True)
    recevingNumber = models.IntegerField(null=True, default=0,blank=True)
    receivingAmount = models.IntegerField(null=True, default=0,blank=True)
    expenceNumber= models.IntegerField(null=True, default=0,blank=True)
    expenceAmount =models.IntegerField(null=True, default=0,blank=True)
    RecLink = models.CharField(max_length=200,null=True,blank=True)
    receiDepPay = models.CharField(max_length=100, null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.FCompany)