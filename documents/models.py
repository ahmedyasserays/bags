from email.policy import default
import numbers
from operator import mod
from xml.dom.minidom import DocumentType
from django.db import models

import documents
from datetime import datetime

# Create your models here.
class uplaodingDocument(models.Model):
    documentNumber = models.IntegerField(null=True, default=0)
    DocumentType = models.CharField(max_length=200)
    itemType = models.CharField(max_length=200)
    documentDate = models.DateField(default=datetime.today)
    file= models.FileField(upload_to="static/")
    def __str__(self):
        return self.DocumentType
    
class newFCompany(models.Model):
    date = models.DateField(default=datetime.today)
    FCompany =models.CharField(max_length=200)
    depostieAmount = models.IntegerField(null=True,blank=True,default=0)
    paymenetAmount = models.IntegerField(null=True,blank=True,default=0)
    DepPAyDate = models.DateField()
    netAmount = models.IntegerField(null=True,blank=True, default=0)
    def __str__(self):
        return self.FCompany
    
class advanceFcompany(models.Model):
    date = models.DateField(default=datetime.today)
    idComapny = models.IntegerField(null=True, default=0,blank=True)
    name =models.CharField(max_length=200)
    recevingNumber = models.IntegerField(null=True, default=0,blank=True)
    receivingAmount = models.IntegerField(null=True, default=0,blank=True)
    expenceNumber= models.IntegerField(null=True, default=0,blank=True)
    expenceAmount =models.IntegerField(null=True, default=0,blank=True)
    depositeAmount = models.IntegerField(null=True, default=0,blank=True)
    paymentAmount = models.IntegerField(null=True, default=0,blank=True)
    DepPayDate = models.DateField()
    FCompany =models.CharField(max_length=200)
    RecLink = models.CharField(max_length=200)
    NetAmount = models.IntegerField(null=True, default=0,blank=True)
    receiDepPay = models.CharField(max_length=100, null=True)
    details = models.TextField()
    notes = models.TextField()
    def __str__(self):
        return self.FCompany